from fastapi import APIRouter, Request, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.async_client import http_client_manager
from app.db.session_maker_fast_api import db_session
from app.tg_bot.handlers import (
    cmd_start, handler_my_appointments, handler_about_us, handler_back_home,
    handler_my_appointments_all,
    )


router = APIRouter(tags=['Webhook'])


@router.post('/webhook')
async def webhook(request: Request, session: AsyncSession = Depends(db_session.get_session)):
    data = await request.json()  # Получаем данные от Telegram
    async with http_client_manager.client() as client:
        if 'message' in data and 'text' in data['message']:
            if data['message']['text'] == '/start':
                user_info = data['message']['from']  # Извлекаем данные пользователя
                await cmd_start(client=client, session=session, user_info=user_info)
        elif 'callback_query' in data:
            callback_query = data['callback_query']
            callback_query_id = callback_query['id']
            chat_id = callback_query['message']['chat']['id']
            callback_data: str = callback_query['data']

            if callback_data.startswith('my_booking_'):
                await handler_my_appointments_all(
                    client=client,
                    callback_query_id=callback_query_id,
                    chat_id=chat_id,
                    session=session,
                    user_db_id=int(callback_data.replace('my_booking_', '')),
                )
            else:
                if callback_data == 'booking':
                    await handler_my_appointments(
                        client=client, callback_query_id=callback_query_id, chat_id=chat_id, session=session
                    )
                elif callback_data == 'about_us':
                    await handler_about_us(client=client, callback_query_id=callback_query_id, chat_id=chat_id)
                elif callback_data == 'home':
                    await handler_back_home(client=client, callback_query_id=callback_query_id, chat_id=chat_id)
        return {'ok': True}
