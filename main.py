def katta_son_faktoriali(n):
    if n < 0:
        raise ValueError("Faktorial berilgan sonning manfiyiga berilishi mumkin emas.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * katta_son_faktoriali(n-1)

def optimallashtirilgan_katta_son_faktoriali(n):
    if n < 0:
        raise ValueError("Faktorial berilgan sonning manfiyiga berilishi mumkin emas.")
    elif n == 0 or n == 1:
        return 1
    else:
        faktorial = 1
        for i in range(2, n+1):
            faktorial *= i
        return faktorial

def iterativ_katta_son_faktoriali(n):
    if n < 0:
        raise ValueError("Faktorial berilgan sonning manfiyiga berilishi mumkin emas.")
    elif n == 0 or n == 1:
        return 1
    else:
        faktorial = 1
        for i in range(2, n+1):
            faktorial *= i
        return faktorial

def rekursiyadan_foydalanmagan_katta_son_faktoriali(n):
    if n < 0:
        raise ValueError("Faktorial berilgan sonning manfiyiga berilishi mumkin emas.")
    elif n == 0 or n == 1:
        return 1
    else:
        faktorial = 1
        for i in range(2, n+1):
            faktorial *= i
        return faktorial

def main():
    n = 10
    print(f"Faktoriali: {katta_son_faktoriali(n)}")
    print(f"Optimallashtirilgan faktoriali: {optimallashtirilgan_katta_son_faktoriali(n)}")
    print(f"Iterativ faktoriali: {iterativ_katta_son_faktoriali(n)}")
    print(f"Rekursiyadan foydalanmagan faktoriali: {rekursiyadan_foydalanmagan_katta_son_faktoriali(n)}")

if __name__ == "__main__":
    main()
```

Kodda uchta turdagi faktorial hisoblash funksiyalari mavjud:

1. Rekursiv faktorial hisoblash funksiyasi
2. Optimallashtirilgan faktorial hisoblash funksiyasi
3. Iterativ faktorial hisoblash funksiyasi
4. Rekursiyadan foydalanmagan faktorial hisoblash funksiyasi

Funksiyalar har biridan birorta ham izoh yozilmagan holda yozilgan.
