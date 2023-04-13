from datetime import date
import tkinter as tk
from refactor_docx import refactor_docx


def start():
    # Необходим, чтобы добавить доп.поля для заполнения места проживания, если регистрация в паспорте с местом
    # проживания не совпадает
    def show_fields():
        tk.Label(win, text='МЕСТО ПРОЖИВАНИЯ', bg='yellow').grid(row=16, column=2, sticky='w')
        tk.Label(win, text='Регион').grid(row=17, column=2, sticky='w')
        tk.Label(win, text='Район').grid(row=18, column=2, sticky='w')
        tk.Label(win, text='Город').grid(row=19, column=2, sticky='w')
        tk.Label(win, text='Населенный пункт').grid(row=20, column=2, sticky='w')
        tk.Label(win, text='Улица').grid(row=21, column=2, sticky='w')
        tk.Label(win, text='Дом').grid(row=22, column=2, sticky='w')
        tk.Label(win, text='Корпус/Строение').grid(row=23, column=2, sticky='w')
        tk.Label(win, text='Квартира').grid(row=24, column=2, sticky='w')
        tk.Label(win, text='Почтовый индекс').grid(row=25, column=2, sticky='w')

        ed_living_region.grid(row=17, column=3)
        ed_living_district.grid(row=18, column=3)
        ed_living_town.grid(row=19, column=3)
        ed_living_locality.grid(row=20, column=3)
        ed_living_street.grid(row=21, column=3)
        ed_living_house.grid(row=22, column=3)
        ed_living_corpus.grid(row=23, column=3)
        ed_living_flat.grid(row=24, column=3)
        ed_living_address_index.grid(row=25, column=3)

    # Если человек живет по месту регистрации, то поля для ввода скрываются
    def hide_fields():
        ed_living_region.grid_forget()
        ed_living_district.grid_forget()
        ed_living_town.grid_forget()
        ed_living_locality.grid_forget()
        ed_living_street.grid_forget()
        ed_living_house.grid_forget()
        ed_living_corpus.grid_forget()
        ed_living_flat.grid_forget()
        ed_living_address_index.grid_forget()

    # При нажатии на кнопку "Отправить" срабатывает скрипт, который создает словари с данными из полей и передает в
    # модуль, который редактирует файл docx
    def submit():
        data = {}
        # словарь с данными договора
        contract_data = {
            'contract_num': f'{str(ed_surname.get())}',
            'date_of_contract': '.'.join(str(date.today()).split('-')[::-1])
        }
        # словарь с данными ОБУЧАЮЩЕГОСЯ
        ed_data = {
            # СВЯЗЬ С ОБУЧАЮЩИМСЯ
            'ed_phone': ed_phone.get(),
            'ed_email': ed_email.get(),
            # информация о контакте ОБУЧАЮЩЕГОСЯ
            'ed_surname': ed_surname.get(),
            'ed_name': ed_name.get(),
            'ed_middlename': ed_middlename.get(),
            'ed_FIO': f'{ed_surname.get()} {ed_name.get()} {ed_middlename.get()}'.upper(),
            'ed_sex': ed_sex.get(),
            'ed_date_of_birth': ed_date_of_birth.get(),
            'ed_town_of_birth': ed_town_of_birth.get(),
            'ed_citizenship': ed_citizenship.get(),
            # данные паспорта ОБУЧАЮЩЕГОСЯ
            'ed_passport_series': ed_passport_series.get(),
            'ed_passport_number': ed_passport_number.get(),
            'ed_passport_index': f'{ed_passport_series.get()} {ed_passport_number.get()}',
            'ed_passport_office': ed_passport_office.get(),
            'ed_passport_date': ed_passport_date.get(),
            'ed_division_code': ed_division_code.get(),
            # адрес регистрации ОБУЧАЮЩЕГОСЯ
            'ed_region': ed_region.get(),
            'ed_district': ed_district.get(),
            'ed_town': ed_town.get(),
            'ed_locality': ed_locality.get(),
            'ed_street': ed_street.get(),
            'ed_house': ed_house.get(),
            'ed_corpus': ed_corpus.get(),
            'ed_flat': ed_flat.get(),
            'ed_address_index': ed_address_index.get(),
            'ed_registration_address': f'{ed_address_index.get()} {ed_region.get()} {ed_district.get()} {ed_town.get()}'
                                       f'{ed_locality.get()} {ed_street.get()} {ed_house.get()} {ed_corpus.get()} {ed_flat.get()}'
        }
        # данные места проживания, который отличается от места регистрации
        living_data = {
            'ed_living_region': ed_living_region.get(),
            'ed_living_district': ed_living_district.get(),
            'ed_living_town': ed_living_town.get(),
            'ed_living_locality': ed_living_locality.get(),
            'ed_living_street': ed_living_street.get(),
            'ed_living_house': ed_living_house.get(),
            'ed_living_corpus': ed_living_corpus.get(),
            'ed_living_flat': ed_living_flat.get(),
            'ed_living_address_index': ed_living_address_index.get(),
            'ed_living_address': f'{ed_living_address_index.get()} {ed_living_region.get()} {ed_living_region} '
                                 f'{ed_living_town} {ed_living_locality} {ed_living_street} {ed_living_house} '
                                 f'{ed_living_corpus} {ed_living_flat}'
        }
        # словарь для данных ОБРАЗОВАТЕЛЬНОЙ ПРОГРАММЫ
        program_data = {
            'education_level': education_level.get(),
            'sublevel_of_education': sublevel_of_education.get(),
            'code_of_program': code_of_program.get(),
            'faculty': faculty.get(),
            'faculty_direction': faculty_direction.get(),
            'full_program_data': f'{code_of_program.get()} {faculty.get()} {faculty_direction.get()}'.upper(),
            'form_of_study': form_of_study.get(),
            'standard_study_duration_sem': standard_study_duration_sem.get(),
            'standard_study_duration_year': standard_study_duration_year.get(),
            'standard_study_duration': f'{standard_study_duration_sem.get()} {standard_study_duration_year.get()}',
            'personal_study_duration_sem': personal_study_duration_sem.get(),
            'personal_study_duration_year': personal_study_duration_year.get(),
            'personal_study_duration': f'{personal_study_duration_sem.get()} {personal_study_duration_year.get()}',
            'cost_of_sem_int': cost_of_sem_int.get(),
            'cost_sem_in_words': cost_sem_in_words.get(),
            'full_cost_of_study_int': full_cost_of_study_int.get(),
            'full_cost_study_in_words': full_cost_study_in_words.get(),
            'start_date_of_study': start_date_of_study.get()
        }
        # Очистка полей после нажатия на кнопку "Отправить"
        # ДАННЫЕ ОБУЧАЮЩЕГОСЯ
        ed_phone.delete(0, 'end')
        ed_email.delete(0, 'end')
        ed_surname.delete(0, 'end')
        ed_name.delete(0, 'end')
        ed_middlename.delete(0, 'end')
        ed_sex.delete(0, 'end')
        ed_date_of_birth.delete(0, 'end')
        ed_town_of_birth.delete(0, 'end')
        ed_citizenship.delete(0, 'end')
        ed_passport_series.delete(0, 'end')
        ed_passport_number.delete(0, 'end')
        ed_passport_office.delete(0, 'end')
        ed_passport_date.delete(0, 'end')
        ed_division_code.delete(0, 'end')
        ed_region.delete(0, 'end')
        ed_district.delete(0, 'end')
        ed_town.delete(0, 'end')
        ed_locality.delete(0, 'end')
        ed_street.delete(0, 'end')
        ed_house.delete(0, 'end')
        ed_corpus.delete(0, 'end')
        ed_flat.delete(0, 'end')
        ed_address_index.delete(0, 'end')

        # МЕСТО ПРОЖИВАНИЯ
        ed_living_region.delete(0, 'end')
        ed_living_district.delete(0, 'end')
        ed_living_town.delete(0, 'end')
        ed_living_locality.delete(0, 'end')
        ed_living_street.delete(0, 'end')
        ed_living_house.delete(0, 'end')
        ed_living_corpus.delete(0, 'end')
        ed_living_flat.delete(0, 'end')
        ed_living_address_index.delete(0, 'end')

        # ПРОГРАММА ОБУЧЕНИЯ
        education_level.delete(0, 'end')
        sublevel_of_education.delete(0, 'end')
        code_of_program.delete(0, 'end')
        faculty.delete(0, 'end')
        faculty_direction.delete(0, 'end')
        form_of_study.delete(0, 'end')
        standard_study_duration_sem.delete(0, 'end')
        standard_study_duration_year.delete(0, 'end')
        personal_study_duration_sem.delete(0, 'end')
        personal_study_duration_year.delete(0, 'end')
        cost_of_sem_int.delete(0, 'end')
        cost_sem_in_words.delete(0, 'end')
        full_cost_of_study_int.delete(0, 'end')
        full_cost_study_in_words.delete(0, 'end')
        start_date_of_study.delete(0, 'end')

        # тут должна быть логика по выбору редактируемого файла и выбора к нему пути, но пока только статика
        path = 'templates/Обучающийся+Исполнитель/договор.docx'

        # объединяю словари
        data.update(contract_data)
        data.update(ed_data)
        data.update(living_data)
        data.update(program_data)

        # отправляю запрос в модуль для редакции шаблона договора
        refactor_docx(path, data, 'filename')

    # Окно приложения
    win = tk.Tk()
    win.title('Планшет АУП')
    win.geometry('1200x900')
    win.minsize(300, 400)
    win.maxsize(1000, 1000)
    win.resizable(True, True)

    # выпадающий список для выбора договора(надо добавить, что добавляются еще поля
    # для ввода данных заказчика и юр. лица)
    # type_of_contract = ['Обуч', 'Обуч+Заказ', 'Обуч+Юр.лиц.']
    # selected_type_of_contract = tk.StringVar()
    # selected_type_of_contract.set(type_of_contract[0])
    # option_menu = tk.OptionMenu(win, selected_type_of_contract, *type_of_contract)
    # option_menu.grid(row=0, column=1)

    # КНОПКА "ОТПРАВИТЬ"
    submit_btn = tk.Button(win, text='Отправить', command=submit)
    submit_btn.grid(row=0, column=2)

    # Лейблы для идентификации полей ОБУЧАЮЩЕГОСЯ
    # лицевая страница паспорта
    tk.Label(win, text='ДАННЫЕ ОБУЧАЮЩЕГОСЯ', bg='green').grid(row=0, column=0, sticky='w')
    tk.Label(win, text='ЛИЦЕВАЯ СТОРОНА ПАСПОРТА', bg='yellow').grid(row=1, column=0, sticky='w')
    tk.Label(win, text='Телефон').grid(row=2, column=0, sticky='w')
    tk.Label(win, text='E-mail').grid(row=3, column=0, sticky='w')
    tk.Label(win, text='Фамилия').grid(row=4, column=0, sticky='w')
    tk.Label(win, text='Имя').grid(row=5, column=0, sticky='w')
    tk.Label(win, text='Отчество').grid(row=6, column=0, sticky='w')
    tk.Label(win, text='Пол').grid(row=7, column=0, sticky='w')
    tk.Label(win, text='Дата рождения').grid(row=8, column=0, sticky='w')
    tk.Label(win, text='Место рождения').grid(row=9, column=0, sticky='w')
    tk.Label(win, text='Гражданство').grid(row=10, column=0, sticky='w')
    tk.Label(win, text='Серия паспорта').grid(row=11, column=0, sticky='w')
    tk.Label(win, text='Номер паспорта').grid(row=12, column=0, sticky='w')
    tk.Label(win, text='Выдан').grid(row=13, column=0, sticky='w')
    tk.Label(win, text='Дата выдачи').grid(row=14, column=0, sticky='w')
    tk.Label(win, text='Код подразделения').grid(row=15, column=0, sticky='w')

    # страница с пропиской
    tk.Label(win, text='СТРАНИЦА С РЕГИСТРАЦИЕЙ', bg='yellow').grid(row=16, column=0, sticky='w')
    tk.Label(win, text='Регион').grid(row=17, column=0, sticky='w')
    tk.Label(win, text='Район').grid(row=18, column=0, sticky='w')
    tk.Label(win, text='Город').grid(row=19, column=0, sticky='w')
    tk.Label(win, text='Населенный пункт').grid(row=20, column=0, sticky='w')
    tk.Label(win, text='Улица').grid(row=21, column=0, sticky='w')
    tk.Label(win, text='Дом').grid(row=22, column=0, sticky='w')
    tk.Label(win, text='Корпус/Строение').grid(row=23, column=0, sticky='w')
    tk.Label(win, text='Квартира').grid(row=24, column=0, sticky='w')
    tk.Label(win, text='Почтовый индекс').grid(row=25, column=0, sticky='w')

    # проживает ли по адресу регистрации или нет ОБУЧАЮЩИЙСЯ
    var = tk.StringVar()
    radio1 = tk.Radiobutton(win, text="Проживает по адресу регистрации", variable=var, value="1", command=hide_fields)
    radio2 = tk.Radiobutton(win, text="Проживает в другом месте", variable=var, value='2', command=show_fields)
    radio1.grid(row=16, column=3)
    radio2.grid(row=16, column=4)

    # Лейблы для Программы обучения(должны работать как выпадающие списки, добавлю позже)
    tk.Label(win, text='ПРОГРАММА ОБУЧЕНИЯ', bg='yellow').grid(row=26, column=0, sticky='w')
    tk.Label(win, text='Уровень образования').grid(row=27, column=0, sticky='w')
    tk.Label(win, text='Подуровень образования').grid(row=28, column=0, sticky='w')
    tk.Label(win, text='Код направления').grid(row=29, column=0, sticky='w')
    tk.Label(win, text='Факультет').grid(row=30, column=0, sticky='w')
    tk.Label(win, text='Направление на факультете').grid(row=31, column=0, sticky='w')
    tk.Label(win, text='Форма обучения').grid(row=32, column=0, sticky='w')
    tk.Label(win, text='Стандартный срок обучения в семестрах').grid(row=33, column=0, sticky='w')
    tk.Label(win, text='Стандартный срок обучения в годах').grid(row=34, column=0, sticky='w')
    tk.Label(win, text='Персональный срок обучения в семестрах').grid(row=35, column=0, sticky='w')
    tk.Label(win, text='Персональный срок обучения в годах').grid(row=36, column=0, sticky='w')
    tk.Label(win, text='Стоимость одного семестра обучения просто цифрой').grid(row=37, column=0, sticky='w')
    tk.Label(win, text='Стоимость одного семестра словами').grid(row=38, column=0, sticky='w')
    tk.Label(win, text='Стоимость всего периода обучения').grid(row=39, column=0, sticky='w')
    tk.Label(win, text='Стоимость всего периода обучения словами').grid(row=40, column=0, sticky='w')
    tk.Label(win, text='Дата начала обучения').grid(row=41, column=0, sticky='w')

    # поля для ввода данных ОБУЧАЮЩЕГОСЯ
    ed_phone = tk.Entry(win)
    ed_email = tk.Entry(win)
    ed_surname = tk.Entry(win)
    ed_name = tk.Entry(win)
    ed_middlename = tk.Entry(win)
    ed_sex = tk.Entry(win)
    ed_date_of_birth = tk.Entry(win)
    ed_town_of_birth = tk.Entry(win)
    ed_citizenship = tk.Entry(win)
    ed_passport_series = tk.Entry(win)
    ed_passport_number = tk.Entry(win)
    ed_passport_office = tk.Entry(win)
    ed_passport_date = tk.Entry(win)
    ed_division_code = tk.Entry(win)

    # поля для ввода данных РЕГИСТРАЦИИ ОБУЧАЮЩЕГОСЯ
    ed_region = tk.Entry(win)
    ed_district = tk.Entry(win)
    ed_town = tk.Entry(win)
    ed_locality = tk.Entry(win)
    ed_street = tk.Entry(win)
    ed_house = tk.Entry(win)
    ed_corpus = tk.Entry(win)
    ed_flat = tk.Entry(win)
    ed_address_index = tk.Entry(win)

    # поля для ввода данных МЕСТА ПРОЖИВАНИЯ ОБУЧАЮЩЕГОСЯ
    ed_living_region = tk.Entry(win)
    ed_living_district = tk.Entry(win)
    ed_living_town = tk.Entry(win)
    ed_living_locality = tk.Entry(win)
    ed_living_street = tk.Entry(win)
    ed_living_house = tk.Entry(win)
    ed_living_corpus = tk.Entry(win)
    ed_living_flat = tk.Entry(win)
    ed_living_address_index = tk.Entry(win)

    # поля для ввода Программы обучения
    education_level = tk.Entry(win)
    sublevel_of_education = tk.Entry(win)
    code_of_program = tk.Entry(win)
    faculty = tk.Entry(win)
    faculty_direction = tk.Entry(win)
    form_of_study = tk.Entry(win)
    standard_study_duration_sem = tk.Entry(win)
    standard_study_duration_year = tk.Entry(win)
    personal_study_duration_sem = tk.Entry(win)
    personal_study_duration_year = tk.Entry(win)
    cost_of_sem_int = tk.Entry(win)
    cost_sem_in_words = tk.Entry(win)
    full_cost_of_study_int = tk.Entry(win)
    full_cost_study_in_words = tk.Entry(win)
    start_date_of_study = tk.Entry(win)

    # поля для ввода данных ОБУЧАЮЩЕГОСЯ
    ed_phone.grid(row=2, column=1)
    ed_email.grid(row=3, column=1)
    ed_surname.grid(row=4, column=1)
    ed_name.grid(row=5, column=1)
    ed_middlename.grid(row=6, column=1)
    ed_sex.grid(row=7, column=1)
    ed_date_of_birth.grid(row=8, column=1)
    ed_town_of_birth.grid(row=9, column=1)
    ed_citizenship.grid(row=10, column=1)
    ed_passport_series.grid(row=11, column=1)
    ed_passport_number.grid(row=12, column=1)
    ed_passport_office.grid(row=13, column=1)
    ed_passport_date.grid(row=14, column=1)
    ed_division_code.grid(row=15, column=1)

    # поля для ввода места регистрации по паспорту ОБУЧАЮЩЕГОСЯ
    ed_region.grid(row=17, column=1)
    ed_district.grid(row=18, column=1)
    ed_town.grid(row=19, column=1)
    ed_locality.grid(row=20, column=1)
    ed_street.grid(row=21, column=1)
    ed_house.grid(row=22, column=1)
    ed_corpus.grid(row=23, column=1)
    ed_flat.grid(row=24, column=1)
    ed_address_index.grid(row=25, column=1)

    # поля для ввода ПРОГРАММЫ ОБУЧЕНИЯ
    education_level.grid(row=27, column=1)
    sublevel_of_education.grid(row=28, column=1)
    code_of_program.grid(row=29, column=1)
    faculty.grid(row=30, column=1)
    faculty_direction.grid(row=31, column=1)
    form_of_study.grid(row=32, column=1)
    standard_study_duration_sem.grid(row=33, column=1)
    standard_study_duration_year.grid(row=34, column=1)
    personal_study_duration_sem.grid(row=35, column=1)
    personal_study_duration_year.grid(row=36, column=1)
    cost_of_sem_int.grid(row=37, column=1)
    cost_sem_in_words.grid(row=38, column=1)
    full_cost_of_study_int.grid(row=39, column=1)
    full_cost_study_in_words.grid(row=40, column=1)
    start_date_of_study.grid(row=41, column=1)

    win.mainloop()


if __name__ == '__main__':
    start()
