import streamlit as st

# Input
a = st.selectbox('人物1', ('唐恺仪','何博文','蔡伯源'))
b = st.selectbox('人物2', ('唐恺仪','何博文','蔡伯源'))

#process
if a == '蔡伯源':
    if  b == '何博文':
        c = (a + '　是　' + b + '　的大儿 ！！！')
    elif b == '唐恺仪':
        c = (a + '　是　' + b + '　的大儿 ！！！')
    else:
        c = ('本人')

elif a == '何博文':
    if  b == '蔡伯源':
        c = (a + '　是　' + b + '　的大爹 ！！！')
    elif b == '唐恺仪':
        c = (a + '　是　' + b + '　的恋人❤')
    else:
        c = ('本人')
else:
    if  b == '何博文':
        c = (a + '　是　' + b + '　的恋人❤')
    elif b == '蔡伯源':
        c = (a + '　是　' + b + '　的母亲 ～～～')
    else:
        c = ('本人')

#output
st.write('三个人的关系')
st.write(c)
