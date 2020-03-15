# moc_ikt
Telegram bot / Test assignment for Junior Python position Developer

Install
apt install -y htop git build-essential libssl-dev libffi-dev python3-pip python3-dev python3-setuptools python3-venv 

Update
git fetch && git checkout -f origin/master 

Тестовое задание на позицию Junior Python Developer:
Напишите диалогового помощника (чат-бота) для мессенджера Telegram на языке программирования Python 3.
Функционал работы чат-бота:
- При вводе команды старт выводится приветственное сообщение, где первый элемент "Добрый", а второй элемент соответствует
времени суток, то есть утро, день, вечер и ночь в зависимости от времени. Также под этим сообщением должна выводиться кнопка
с названием "Список производителей электроники:".
- При нажатии на кнопку - "Список производителей электроники:", должен быть переход по кнопке в сам список производителей электроники, который представлен ниже:
electronics_list = ['Apple', 'Samsung', 'Nokia', 'Sony', 'Canon', 'Panasonic', 'Bose', 'Microsoft', 'LG', 'Intel', 'Nvidia', 'Dell', 'IBM', 'Acer', 'Asus', 'Lenovo', 'Xiaomi', 'Huawei']
Список должен выводиться с сортировкой по алфавиту и пронумерован, а также должна быть сделана пагинация по 10 элементов списка на сообщение и внизу должны быть кнопки:
	- "Назад", осуществляющая переход на приветственное сообщение;
	- ">>", осуществляющая переход на следующее сообщение с оставшимися элементами списка;
	Пример вывода: "Список производителей электроники:
				1. Acer
				2. Apple
				..."
- При нажатии на кнопку ">>" переход осуществляется на оставшиеся элементы списка (важно: при переходе должна осуществляться замена предыдущего сообщения на новое,
то есть сообщение со списком первых 10 элементов заменяется на сообщение с оставшимися элементами списка), а также добавлена кнопка "Назад", которая осуществляет переход
на приветственное сообщение.
