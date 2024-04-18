def small_words(str):

    words = str.split()
    short_words = [word for word in words if len(word) < 5]

    return short_words

input_string = "Было просто пасмурно, дуло с севера А к обеду насчитал сто градаций серого Так всегда первого ноль девятого То ли весь мир сошёл с ума, то ли я - того На столе записка от неё смятая  Недопитый виски допиваю с матами Посмотрю в окно, допишу главу Первое сентября, дворник жжёт листву Серым облакам наплевать на нас Если знаешь как жить - живи Ты хотела плыть как все - так плыви"
result = ' ' .join(small_words(input_string))
print("Words with length less than 5:", result)
