import streamlit as st
import numpy as np
import pandas as pd
#画像を表示させるためのライブラリ
from PIL import Image

st.title('Streamlit　超入門')# これでタイトルを表示することができます。

st.write("DataFrame")#テキストを表示させる
st.write("Display image")

img = Image.open("/Users/sugawara_yuuki/Desktop/yuki_MacBook_Pro/Udemy/Streamlit_udemy/abe_hiroshi.jpeg")#画像のpathを入力
#画像の表示,第3引数はレイアウトの大きさに合わせて表示する
st.image(img, caption="abe_hiroshi", use_column_width=True)

df = pd.DataFrame(
   np.random.rand(20,3),#20個のランダムな値を３つ生成
   columns=["a", "b", "c"]
)

#st.write(df)これでもDataFrameを表示させることができる
#しかし下記においては。引数で大きさを変更可能(width,heightで指定)
#dfのみで表示可能だが、df.style.highlight_max()'は列、または行の最大値をハイライトする。
#axis=0は列を指定する。１の場合は行
# 動的なDataFrameの表示→st.dataframe(df.style.hight_max(axis=0))


#静的なDataFrameの表示
#st.table(df.style.highlight_max(axis=0))


#折れ線グラフでのプロット※使い方は公式ドキュメント、APIリファレンス参照
st.line_chart(df)
st.bar_chart(df)


#mapのプロット(新宿区を参考にする)
df2 = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69, 139.70],
    columns=["lat","lon"]
)
st.map(df2)#これで地図上にプロットできる。緯度、軽度さえわかればいいので多機能である。