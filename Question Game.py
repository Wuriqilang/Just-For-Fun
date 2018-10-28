#
# Question Game.py
# @author Wuriqilang
# @description 
# @created Sun Oct 28 2018 14:30:33 GMT+0800 (中国标准时间)
# @last-modified Sun Oct 28 2018 15:54:24 GMT+0800 (中国标准时间)
#
import os
import json
import sys


def to_answer(letter,c_len):
    letter=letter.upper()
    if len(letter) == 1 and 'A'<= letter <= 'Z':
        digit = ord(letter)-ord('A')
        if 0 <= digit < c_len:
            return digit,True
        else:
            return None,False
    else:
        return None,False

def to_letter(n):
    return chr(ord('A')+n)

def ask_question(question,i):
    print('\n第{0}题:{1}'.format(i,question['question']))
    choices = question['choices']
    c_len = len(choices)
    for j in range(c_len):
        print('{0}:{1}'.format(to_letter(j),choices[j]))
    user_input = input('请输入答案:')
    user_answer,ok=to_answer(user_input,c_len)
    while not ok:
        user_input = input('输入错误,请输入选项:')
        user_answer,ok =to_answer(user_input,c_len)
    return user_answer == question['answer']

def read_question_file(filename):
    if not os.path.isfile(filename):
        return None
    with open(filename,'r',encoding="utf-8") as f:
        try:
            return json.load(f)
        except ValueError as e:
            print(e)
            print('加载题库错误')
            return None


def main():


    # 定义题库列表, 每道题目为一个字典
    filename='sample_question.json'
    question_json = read_question_file(filename)
    if not question_json:
        print('题库文件读取失败,请检查{0}'.format(filename))
        sys.exit(-1)
        
    name = question_json['name']
    question_list = question_json['question_list']

    print('答题开始,题库为{0}'.format(name))
 
    # 展示题目,提示用户输入判断答案
    q_len = len(question_list)
    correct_count = 0
    for i,q in enumerate(question_list):
        if ask_question(q,i):
            correct_count += 1
    # 计算并展示正确率
    print('\n答题完成,共{0}道题目,你答对了{1}题,争取率{2:.2f}%'.format(q_len,correct_count,correct_count/q_len*100))
    


if __name__ == '__main__':
    main()