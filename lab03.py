import re

slct = 1
while slct != 0:
    print("Task 1 -> 1"
          "\nTask 2 -> 2 "
          "\nTask 3 -> 3 "
          "\nTask 4 -> 4 "
          "\nTask 5 -> 5"
          "\nTask 6 -> 6"
          "\nTask 7 -> 7"
          "\nTask 8 -> 8"
          "\nTask 9 -> 9"
          "\nTask 10 -> 10"
          "\nTask 11 -> 11"
          "\nTask 12 -> 12"
          "\nTask 13 -> 13"
          "\nExit 0 -> 0")

    slct = int(input("\n Виберіть пункт:"))

    match slct:
        case 1:
            print("\nTask 1")
            someText = input("Введіть текст:").lower()
            letter = input("Введіть літеру:").lower()
            print(f"Кількість входжень: {len(re.findall(rf'{letter}[а-я]+', someText))}\n")

        case 2:
            print("\nTask 2")
            someText = input("Введіть текст:")
            print(f"Змінений текст: {someText.replace(':', '%')}\n")

        case 3:
            print("\nTask 3")
            someText = input("Введіть текст:")
            count = someText.count('.')
            editedText = someText.split('.')
            print(f"Кількість видалень: {count}\n"
                  f"Змінений текст: {''.join(editedText)}\n")

        case 4:
            print("\nTask 4")
            someText = input("Введіть текст:")
            count = someText.count('a')
            print(f"Кількість замін: {count}"
                  f"\nЗмінений текст: {someText.replace('a', 'o')}"
                  f"\nДовжина рядка: {len(someText)}\n")

        case 5:
            print("\nTask 5")
            someText = input("Введіть текст:")
            print(f"Змінений текст:{someText.lower()}\n")

        case 6:
            print("\nTask 6")
            someText = input("Введіть текст:")
            count = someText.count('o')
            editedText = someText.split('o')
            print(f"Кількість видалень: {count}\nЗмінений текст: {''.join(editedText)}\n")

        case 7:
            print("\nTask 7")
            someText = input("Введіть текст:")
            splitText = [someText[:int(len(someText) / 2)], someText[int(len(someText) / 2):]]
            splitText[0] = splitText[0].replace('п', '*')
            print(f"Змінений текст: {''.join(splitText)}\n")

        case 8:
            print("\nTask 8")
            someText = input("Введіть текст:")
            word = input("Введіть слово:")
            print(f"Кількість входжень: {someText.count(word)}\n")

        case 9:
            print("\nTask 9")
            someText = input("Введіть текст:")
            print(f"Змінений текст: {someText.title()}\n")

        case 10:
            print("\nTask 10")
            someText = input("Введіть текст:")
            N = input("Введіть N:")
            P = input("Введіть P:")
            Nwords = re.findall(rf"{N}[A-Za-z]+", someText)
            wordsP = re.findall(rf"[A-Za-z]+{P}", someText)
            print(f"Слова що починаються на {N}:{Nwords}"
                  f"\nСлова що закінчуються на {P}:{wordsP}", )

        case 11:
            print("\nTask 11")
            someText = input("Введіть текст:").lower()
            print(f"Кількість голосних в тексті: {len(re.findall(rf'[aeiou]', someText))}", )

        case 12:
            print("\nTask 12")
            someText = input("Введіть текст:").lower()
            print(f"Кількість приголосних в тексті: {len(re.findall(rf'[qwrtypsdfghjklzxcvbnm]', someText))}", )

        case 13:
            print("\nTask 13")
            someText = input("Введіть текст:")
            print(f"Список всіх власних назв і імен в тексті: {re.findall(r'[A-Z][a-z]+', someText)}")
