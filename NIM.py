def integrate(a, b, n, func, method='ls'): #функция нахождения интеграла одним из пяти методов, на заданном количестве шагов
    result = 0
    step = (b-a)/n
    if method == 'ls': #метод левых прямоугольников
        while a < b:
            result += func(a)
            a += step
        return result * step

    if method == 'rs': #метод правых прямоугольников
        while a <= b:
            a += step
            result += func(a)
        return result * step

    if method == 'cs': #метод центральных прямоугольников
        while a < b:
            result += func((a+a+step)/2)
            a += step
        return result * step
    
    if method == 'tr': #метод трапеций
        while a < b:
            result += (func(a) + func(a+step))/2
            a += step
        return result * step

    if method == 'simp': #метод Симпсона
        result = func(a) + func(b)
        i = 1
        a += step
        even = 0
        odd = 0
        while a < b:
            if i % 2 == 0:
                even += func(a)
            elif i % 2 == 1:
                odd += func(a)
            a += step
            i += 1
        return (result + 4 * odd + 2 * even) * 2 * step / 6 
