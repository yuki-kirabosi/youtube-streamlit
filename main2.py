import streamlit as st

#画像を表示させるためのライブラリ
from PIL import Image
import time

st.title('Streamlit　超入門')# これでタイトルを表示することができます。

st.write("DataFrame")#テキストを表示させる
st.write("プログレスバーの表示")
"Start!!"

latest_iteration = st.empty()
#progresbarを初期化して代入、引数は初期値
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.05)

left_column, right_column = st.beta_columns(2)
button = left_column.button("右カラムに表示")
if button:
    right_column.write("ここは右カラム")


#expanderを使うことでクリック後に表示させることができる
expander=st.beta_expander('問い合わせ')
expander.write("問い合せ内容を書く")

#　チェックボックスの作成(チェックボックスにチェックがあれば画像を表示させる)
#if st.checkbox("Show Image"):
#   img = Image.open("/Users/sugawara_yuuki/Desktop/yuki_MacBook_Pro/Udemy/Streamlit_udemy/abe_hiroshi.jpeg")#画像のpathを入力
   #画像の表示,第3引数はレイアウトの大きさに合わせて表示する
#   st.image(img, caption="abe_hiroshi", use_column_width=True)

#option = st.selectbox(
#    "あなたが好きな数字を教えてください、",
#   list(range(1,11))
#)


# テキスト
#text = st.text_input("あなたの趣味を教えてください。")
#"あなたの趣味は、",text,"です。"

#st.sliderは、テキストの次の引数に開始数値、次に上限数値、デフォルト数値の順で設定する
#condition = st.slider("あなたの今の調子は？",0 , 100 ,50)
#"コンディション：",condition

# サイドバーの利用方法
#text = st.sidebar.text_input("あなたの趣味を教えてください。")
#condition = st.sidebar.slider("あなたの今の調子は？",0 , 100 ,50)


#"あなたの趣味は、",text,"です。"
#"コンディション：",condition




