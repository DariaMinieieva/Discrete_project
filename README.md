# Тема 6. Аналіз відношень
 
Ми виконували проект при використанні Python 3. Для виконання проекту нам знадобилися знання з теми “Відношення” з курсу дискретної математики. **Розподіл роботи** в команді був такий:
* Завдання 1 - Ганна Єршова 
* Завдання 2 - Ольга Люба 
* Завдання 3, 4 - Дар'я Мінєєва 
* Завдання 5 - Анна-Аліна Бондарець 
* Завдання 6 - Вікторія Рой 

Для комунікації використовували чат в Телеграмі, відео-зв’язки на основі Google Meet, для написання спільного коду використовували репозиторій GitHub. 

## Опис завдань
**Завд. 1.** Читання відношення з файлу, запис відношення в файл. Формат файлу -csv, nxn матриця, яка репрезентує відношення.
Було розроблено дві функції:
1. для читання матриці з файлу(read_file(path: str) -> list):
1. функція читає файл, у якому записана матриця, та повертає її у форматі списку списків
для запису матриці у файл(write_file(matrix: list, path='matrix.csv'))

**Завд. 2.** Пошук симетричного та рефлексивного замикання відношень. Функції
повинні повертати матриці замикань, які можна записати у файл у вигляді
відношень.
Було розроблено 2 функції:
1. для пошуку рефлексивного замикання (reflexive_closure(matrix: list) -> list): рефлексивне замикання R дорівнює R∪∆, де ∆={(a, a): a∈A}, тобто в матриці на позиціях з однаковими індексами рядка і стовпця мають стояти одиниці. Ця функція повертає список (матрицю) - рефлексивне замикання відношення.
1. для пошуку симетричного замикання (symmetric_closure(matrix: list) -> list): для отримання симетричного замикання потрібно додати всі такі пари (b, a), що (b, a)∉R, але (a, b)∈R, тобто потрібно розміщувати одиниці на позиціях, де номер рядка і номер стовпця дорівнюють номеру стовпця і номеру рядка тих позицій, де є одиниці, відповідно. Ця функція повертає список (матрицю) - симетричне замикання відношення.

**Завд. 3.** Пошук транзитивного замикання відношень. Для пошуку замикання було використано алгоритм Воршалла (версія 2, лекція 6).  
Функція warshall_algorithm(matrix: list) -> list приймає список списків, який представляє матрицю та повертає транзитивне замикання цієї матриці.

**Завд. 4.** Перевірка чи відношення є транзитивним. Дана функція (check_transitive_closure(matrix: list) -> bool) приймає матрицю та перевіряє її транзитивність за допомогою алгоритму Воршалла. Для пришвидшення алгоритму було здійснено перевірку, якщо хоча б один 0 буде змінено на 1, то матриця не транзитивна, отже немає змісту продовжувати виконання функції. Якщо матриця транзитивна, то складність залишиться такою ж, як і у звичайного алгоритму Воршалла.

**Завд. 5.** Розбиття відношення еквівалентності на класи еквівалентності. Повертає список класів еквівалентності (кожен клас також список).

Відношення на множині A називають відношенням еквівалентності, якщо воно рефлексивне, симетричне й транзитивне. Два елементи множини А, пов’язані відношенням еквівалентності, називають еквівалентними.

Нехай R – відношення еквівалентності на множині А. Множину всіх елементів, які еквівалентні до елемента a∈A, називають класом еквівалентності (елемента а) за відношенням R. 

Кожне відношення еквівалентності R на множині А породжує розбиття множини А на класи еквівалентності. 

Елементи, що належать одному класу еквівалентності, попарно еквівалентні між собою. Отже, стовпці матриці відношення еквівалентності для елементів одного класу еквівалентності однакові та містять одиниці у всіх рядках, які відповідають цим елементам. Оскільки класи еквівалентності не перетинаються, у стовпцях, які відповідають елементам різних класів, не буде одиниць в одних і тих самих рядках.

Було розроблено 5 функцій:
1. find_indexes(matrix: list) -> list
Створює список із кортежів, що містять елементи матриці, подані відповідними латинськими буквами до ненульового елементу матриці. 
```
find_indexes([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
[('a0', 'a0'), ('a0', 'a1'), ('a0', 'a2'), ('a1', 'a0'), ('a1', 'a1'), ('a1', 'a2'), ('a2', 'a0'), ('a2', 'a1'), ('a2', 'a2')]
find_indexes([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
[]
```
2. find_matrix_elements(matrix: list), find_elements_amount(all_elements: list, unique_elements: list) та find_all_classes(tuples_list: list) – допоміжні функції для знаходження класів еквівалентності, використовуючи списки кортежів.
find_equivalence_classes(matrix: list) -> list
3. Головна функція, що викликає усі попередні й у кінцевому випадку повертає список із усіх класів еквівалентності. Аргумент matrix – матриця, подана як список списків. 
```
find_equivalence_classes([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
[['a0', 'a1', 'a2']]
find_equivalence_classes([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 1]])
[['a0', 'a1'], ['a2', 'a3'], ['a4']]
```

**Завд. 6**
Повертає кількість усіх різних транзитивних відношень на множині з n елементів.

Відношення R на множині A називають транзитивним, якщо для будь-яких a, b, c ∈ A з того, що (a, b) ∈ R і (b, c) ∈ R, випливає (a, c) ∈ R.
Для перевірки матриці на транзитивність використовувалась перевірка алгоритмом Воршалла (4 функція)
Матриці генеруються порядково, на кожному кроці відкидаються не транзитивні матриці

Було розроблено 2 функції:
1. count_of_transitive_relations (elements: int) -> int
Головна функція, що приймає кількість елементів у множині та повертає кількість усіх різних транзитивних відношень на цій множині
```
count_of_transitive_relations(2)
13
count_of_transitive_relations(3)
171
```
2. generate_fragment (length: int, fragment: list, counter: int = 0) -> list:
Допоміжна рекурсивна функція, що генерує усі можливі бінарні рядки розміром lenght та повертає список з ними
```
generate_fragment(1, [0])
[[0], [1]]
generate_fragment(2, [0, 0])
[[0, 0], [0, 1], [1, 0], [1, 1]]
```


## Висновок
У ході виконання завдання ми покращили свої знання з дискретної математики, а також навчилися застосувати їх на практиці. Як результат, отримали повноцінну бібліотеку, що працює із відношеннями, поданими через їх матриці. Дана бібліотека може зчитувати та записувати матрицю в файл, шукати симетричне, рефлексивне та транзитивне замикання матриці, перевіряти чи відношення, задане матрицею, транзитивне, розбивати відношення на класи еквівалентності та знаходити кількість транзитивних відношень для множин з кількістю елементів n.

