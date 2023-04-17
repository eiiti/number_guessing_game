import streamlit as st
import numpy as np

def main():
    st.title("数当てゲーム")
    st.write("1から100までの数を当ててください。10回の試行が与えられます。")

    # セッション情報を保存する
    if "number_to_guess" not in st.session_state:
        st.session_state.number_to_guess = np.random.randint(1, 101)
    if "guess_count" not in st.session_state:
        st.session_state.guess_count = 0
    if "game_over" not in st.session_state:
        st.session_state.game_over = False

    # ゲームが終了していない場合
    if not st.session_state.game_over:
        guess = st.number_input("あなたの予想を入力してください（1～100）", min_value=1, max_value=100)

        if st.button("予想を提出"):
            st.session_state.guess_count += 1

            if guess == st.session_state.number_to_guess:
                st.success(f"正解！ {st.session_state.number_to_guess} です！")
                st.balloons()
                st.session_state.game_over = True
            elif st.session_state.guess_count >= 10:
                st.error(f"残念！10回の試行が終了しました。正解は {st.session_state.number_to_guess} でした。")
                st.session_state.game_over = True
            elif guess < st.session_state.number_to_guess:
                st.warning("もっと大きい数を試してください。")
            else:
                st.warning("もっと小さい数を試してください。")
    else:
        if st.button("もう一度遊ぶ"):
            st.session_state.number_to_guess = np.random.randint(1, 101)
            st.session_state.guess_count = 0
            st.session_state.game_over = False

if __name__ == "__main__":
    main()
