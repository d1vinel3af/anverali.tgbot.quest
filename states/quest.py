from aiogram.fsm.state import State, StatesGroup




class FormSendQuest(StatesGroup):
    quest_text = State()