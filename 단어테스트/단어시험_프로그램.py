import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
import csv
import random

words_list = []
question_count = 0
correct_answers = 0
incorrect_words = []

## STEP 1 함수

# 단어 저장 [csv 파일 불러오기[
def load_csv():
    global words_list
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            words_list = list(reader)
            print(f"CSV file loaded: {file_path}")
            messagebox.showinfo("성공", "CSV 파일이 성공적으로 저장되었습니다.")
    else:
        messagebox.showwarning("경고", "파일이 선택되지 않았습니다.")

# 저장된 단어 확인 [단어 저장 확인]
def check_saved_words():
    if words_list:
        top = tk.Toplevel()
        top.title("저장된 단어")
        
        # Treeview
        columns = ("단어", "의미")
        treeview = ttk.Treeview(top, columns=columns, show="headings")
        treeview.pack(pady=10)

        for col in columns:
            treeview.heading(col, text=col)

        for word, meaning in words_list:
            treeview.insert("", "end", values=(word, meaning))
    else:
        messagebox.showinfo("알림", "저장된 단어가 없습니다.")


## STEP 2 함수

# 변수 초기화 및 단어 테스트 모드 결정
# 새로운 단어 테스트를 위해 매번 변수 초기화
def start_new_test(test_type):
    global question_count, correct_answers, incorrect_words
    question_count = 0
    correct_answers = 0
    incorrect_words = []

    if test_type == "spelling":
        spelling_test()
    elif test_type == "meaning":
        meaning_test()

# [단어 스펠링 맞히기] (10번 시행)
def spelling_test():
    global question_count, correct_answers

    if not words_list:
        messagebox.showwarning("경고", "저장된 단어가 없습니다.")
        return

    if question_count == 10:
        messagebox.showinfo("시험 종료", f"총 정답 갯수: {correct_answers}/10")
        return

    word, meaning = random.choice(words_list)
    question_text = f"'{meaning}'의 스펠링을 입력하세요:"

    user_answer = simpledialog.askstring("질문", question_text)
    if user_answer is not None:
        check_answer_spelling_test(word, meaning, user_answer)

# 정답 확인 및 틀린 단어 저장
def check_answer_spelling_test(word, meaning, user_answer):
    global question_count, correct_answers, incorrect_words

    if user_answer.lower() == word.lower():
        correct_answers += 1
        messagebox.showinfo("결과", "정답입니다!")
    else:
        messagebox.showinfo("결과", f"오답입니다. 정답은 '{word}'입니다.")
        if (word, meaning) not in incorrect_words:
            incorrect_words.append((word, meaning)) # (중복 방지를 위해 incorrect_words에 이미 저장된 단어는 제외)

    question_count += 1
    spelling_test()

# [단어 뜻 맞히기] (10번 시행)
def meaning_test():
    global question_count, correct_answers

    if not words_list:
        messagebox.showwarning("경고", "저장된 단어가 없습니다.")
        return

    if question_count == 10:
        messagebox.showinfo("시험 종료", f"총 정답 갯수: {correct_answers}/10")
        return

    word, meaning = random.choice(words_list)
    question_text = f"'{word}'의 뜻을 입력하세요:"

    user_answer = simpledialog.askstring("질문", question_text)
    if user_answer is not None:
        check_answer_meaning_test(word, meaning, user_answer)
        
# 정답 확인 및 틀린 단어 저장    
def check_answer_meaning_test(word, meaning, user_answer):
    global question_count, correct_answers, incorrect_words

    if user_answer.lower() == meaning.lower():
        correct_answers += 1
        messagebox.showinfo("결과", "정답입니다!")
    else:
        messagebox.showinfo("결과", f"오답입니다. 정답은 '{meaning}'입니다.")
        if (word, meaning) not in incorrect_words:
            incorrect_words.append((word, meaning)) # (중복 방지를 위해 incorrect_words에 이미 저장된 단어는 제외)

    question_count += 1
    meaning_test()

## STEP 3 함수

# 틀린 단어 csv파일로 저장 [틀린 단어 저장하기]
def save_incorrect_words_to_csv():
    if not incorrect_words:
        messagebox.showinfo("정보", "저장할 틀린 단어가 없습니다.")
        return
    
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_path:
        with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Word", "Meaning"])
            writer.writerows(incorrect_words)
            messagebox.showinfo("성공", "틀린 단어들이 CSV 파일로 저장되었습니다.")
    else:
        messagebox.showwarning("경고", "파일이 저장되지 않았습니다.")

# 틀린 단어 확인 [틀린 단어 저장 확인]
def check_incorrect_words():
    if incorrect_words:
        top = tk.Toplevel()
        top.title("틀린 단어")
        
        # Treeview
        columns = ("단어", "의미")
        treeview = ttk.Treeview(top, columns=columns, show="headings")
        treeview.pack(pady=10)

        for col in columns:
            treeview.heading(col, text=col)

        for word, meaning in incorrect_words:
            treeview.insert("", "end", values=(word, meaning))
    else:
        messagebox.showinfo("알림", "틀린 단어가 없습니다.")

## 프로그램 종료
def close_program():
    root.destroy()

# ---------------------------------------------------------------------
## 본문

root = tk.Tk()
root.title("단어 테스트")
root.geometry("400x500")  # Set window size

label_title = tk.Label(root, text="단어 테스트", font=("Arial", 16))
label_title.pack(pady=10)


## STEP 1
step1 = tk.Frame(root)
step1.pack(pady=10)

label_step1 = tk.Label(step1, text="STEP 1\n단어를 저장하세요", font=("Arial", 12))
label_step1.pack(anchor="center", pady=5)

btn_load_csv = tk.Button(step1, text="csv 파일 불러오기", command=load_csv)
btn_load_csv.pack(side="left", padx=10)

btn_check_words = tk.Button(step1, text="단어 저장 확인", command=check_saved_words)
btn_check_words.pack(side="left", padx=10)

## STEP 2
step2 = tk.Frame(root)
step2.pack(pady=10)

label_step2 = tk.Label(step2, text="STEP 2\n단어 시험을 보세요", font=("Arial", 12))
label_step2.pack(anchor="center", pady=5)

btn_spelling_test = tk.Button(step2, text="단어 스펠링 맞히기", command=lambda: start_new_test("spelling"))
btn_spelling_test.pack(side="left", padx=10)

btn_meaning_test = tk.Button(step2, text="단어 뜻 맞히기", command=lambda: start_new_test("meaning"))
btn_meaning_test.pack(side="left", padx=10)

## STEP 3
step3 = tk.Frame(root)
step3.pack(pady=10)

label_step3 = tk.Label(step3, text="STEP 3\n틀린 단어를 저장해서 복습해 보세요", font=("Arial", 12))
label_step3.pack(anchor="center", pady=5)

btn_save_incorrect = tk.Button(step3, text="틀린 단어 저장하기", command=save_incorrect_words_to_csv)
btn_save_incorrect.pack(side="left", padx=10)

btn_check_incorrect = tk.Button(step3, text="틀린 단어 저장 확인", command=check_incorrect_words)
btn_check_incorrect.pack(side="left", padx=10)

## 종료
btn_exit = tk.Button(root, text="종료", command=close_program)
btn_exit.pack(pady=20)

root.mainloop()
