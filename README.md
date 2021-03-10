# Численные методы интегрирования
Функция `integrate` позволяет вычислять интеграл одним из методов:
- Метод левых прямоугольников
- Метод правых прямоугольников
- Метод центральных прямоугольников
- Метод трапеций
- Метод Симпсона

***

## Синтаксис
**integrate(a, b, n, func, method='ls')**
### Параметры:
#### a : int,float
Левая граница интеграла.
#### b : int,float
Правая граница интеграла.
#### n : int
Количество разбиений.
#### func : callable
Подынтегральная функция.
#### method : str,optional
Метод вычисления. Должен быть одним из
- 'ls' 
- 'rs'
- 'cs'
- 'tr'
- 'simp'

По соответствию с перечисленным выше. По умолчанию - 'ls'.
