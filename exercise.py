# -*- coding: utf-8 -*-
# 練習問題
# https://gotutiyan.hatenablog.com/entry/2020/04/14/174007#1-%E5%A4%89%E6%95%B0

# 1. 変数
def ex_1():
    x = 2
    print(x * 3)

# 2. swap
def ex_2():
    a = 100
    b = 200
    print('before swapping: {} {}'.format(a, b))
    a, b = b, a
    print('after swapping: {} {}'.format(a, b))

# 3. 四則演算+α
def ex_3():
    a = 10
    b = 2
    print('{} {} {} {}'.format(a+b, a-b, a*b, a/b))

# 4. 余り
def ex_4():
    a = 5
    b = 3
    print('{}'.format(a%b))

# 5. べき乗
def ex_5():
    a = 5
    b = 10
    print('{}'.format(a**b))

# 6. if，比較演算子<, >
def ex_6():
    a = 5
    b = 10
    print('{}'.format(a if a > b else b))

# 7. 比較演算子==, bool
def ex_7():
    a = 5
    print('{}'.format(a % 2 == 0))

# 8. 文字列（ランダムアクセス）
def ex_8():
    s = 'python'
    print(s[2])

# 9. 文字列（結合）
def ex_9():
    str_a = 'py'
    str_b = 'thon'
    print(str_a + str_b)
    
#10. 文字列（format）
def ex_10():
    a = 5
    b = 3
    print('{}%{}={}'.format(a, b, a%b))

# 11. 文字列（replace）
def ex_11():
    s = 'some1'
    print(s.replace('1', 'one'))
    
# 12. 文字列（lower）
def ex_12():
    s = 'This Is A Sentence .'
    print(s.lower())
    
# 13. 文字列（upper）
def ex_13():
    s = 'This Is A Sentence .'
    print(s.upper())
    
# 14. 文字列（文字数）
def ex_14():
    s = 'How many characters?'
    print(len(s))
    
# 15. 文字列 → 数値
def ex_15():
    a = '34'
    b = '43'
    print(int(a) + int(b))
    
# 16. リスト
def ex_16():
    lst = [1, 2, 3, 4, 5]
    print(lst[3])
    
# 17. リスト（結合）
def ex_17():
    li1 = [1, 2, 3]
    li2 = [4, 5]
    print(li1 + li2)
    
# 18. リスト（append）
def ex_18():
    lst = [1, 2, 3, 4, 5]
    lst.append(6)
    lst.append(7)
    print(lst)

# 19. リスト（insert）
def ex_19():
    lst = [1, 2, 3, 4, 5]
    lst.insert(1, 100)
    print(lst)
    
# 20. リスト（forによる走査）
def ex_20():
    lst = [1, 2, 3, 4, 5]
    for num in lst:
        if num % 2 == 0:
            print('{} '.format(num), end='')
            
# 21. リスト（forによる走査, enumerate）
def ex_21():
    lst = [1, 2, 3, 4, 5]
    for i, elem in enumerate(lst):
        if i % 2 == 0:
            print('{} '.format(elem), end='')

# 22. リスト（len）
def ex_22():
    lst = [11, 22, 33, 44, 55, 66]
    print(len(lst))

# 23. リスト，if（存在確認）
def ex_23():
    lst = [11, 22, 33, 44, 55]
    for elem in lst:
        if elem == 44:
            print(True)
            return
    print(False)
        
# 24. タプル，リストの負のindex
def ex_24():
    lst = [1, 2, 3, 4, 5]
    tpl = (lst[0], lst[-1])
    print(tpl)

# 25. 辞書
def ex_25():
    dct = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
    print(dct)
    
# 26. 辞書（keys）
def ex_26():
    dct = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
    print(list(dct.keys()))
    
# 27. 辞書（values）
def ex_27():
    dct = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
    print(list(dct.values()))
    
# 28. 辞書（items）
def ex_28():
    dct = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
    print(list(dct.items()))

# 29. 辞書（キーの存在確認）
def ex_29():
    d = {'apple':10, 'grape':20, 'orange':30}
    d.setdefault('apple', -1)
    d.setdefault('pineapple', -1)
    print(d)

# 30. スライス1
def ex_30():
    s = 'training'
    print(s[1:5])

# 31. スライス2
def ex_31():
    s = 'understand'
    print(s[1::2])

# 32. スライス3
def ex_32():
    lst = [1, 2, 3, 4, 5]
    print(lst[::-1])

# 33. 集合
def ex_33():
    lst = [1, 1, 2, 3, 3, 4, 5]
    print(set(lst))

# 34. 積集合
def ex_34():
    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 4, 5, 6, 7}
    print(set1 & set2)

# 35. 和集合
def ex_35():
    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 4, 5, 6, 7}
    print(set1 | set2)

# 36. 差集合
def ex_36():
    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 4, 5, 6, 7}
    print(set1 - set2)

# 37. 型の確認
def ex_37():
    data1 = {'A':1, 'B':2}
    data2 = "hoge"
    data3 = {1,2,3,4,5}
    print('{} {} {}'.format(type(data1), type(data2), type(data3)))

# 38. strip
def ex_38():
    s = 'This is sentence .\n'
    print(s.strip('\n'))

# 39. split
def ex_39():
    s = 'C C++ // python java'
    print(s.split(' '))
    print(s.split('/'))

# 40. join
def ex_40():
    lst = ['This', 'is', 'a', 'sentence']
    print(' '.join(lst))
# 41. max
# 42. min
# 43. sum
# 44. 昇順ソート
# 45. ラムダ式
# 46. range()
# 47. 内包表記
# 48. 例外処理
# 49. ビット演算
# 50. モジュールのインポート
# 演習1（forのネスト）
# 演習2（辞書の値ソート）
# 演習3（num2freq）
# 演習4（word2freq）
# 演習5（Jaccard係数）

def main():
    ex_40()

if __name__ == '__main__':
    main()