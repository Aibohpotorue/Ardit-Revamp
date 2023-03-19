import streamlit as st
from modules import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["todo_input_box"].title()
    todos.append(todo + '\n')
    functions.write_todos(todos)
    st.session_state["todo_input_box"] = ''

todos = functions.get_todos()

st.title('Ardit Todo App')
st.subheader('Harvest your inner dilligence!')
st.write("A tool to increase one's productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox: # = True:?
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='Enter a todo:', placeholder='Add new Todo...',
              on_change=add_todo, key="todo_input_box")

st.session_state
