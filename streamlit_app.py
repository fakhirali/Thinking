'''
Able to add statements to the decision
Drop down for support and refute
Two drop downs for the support and refute
'''


import streamlit as st
from decisions import Decision, Statement, make_graph

if 'decision' not in st.session_state:
    d = Decision('Mortality of Socrates', 'Is Socrates mortal?')
    st.session_state['decision'] = d
else:
    d = st.session_state['decision']

# print([s.supports for s in d.statements])

g = make_graph(d.statements)
g.render(format='jpg')
# text box and button to add statement

#image of the logic graph from the jpg
st.image('hello.gv.jpg')

st.write('Add a statement')
statement = st.text_input('Statement')
add_statement = st.button('Add Statement')
if add_statement:
    s = Statement(statement)
    d.statements.append(s)
    st.rerun()


stmt = st.selectbox('Select a statement', range(len(d.statements)), format_func=lambda x: d.statements[x])
delete_stmt_btn = st.button('Delete Statement')
if delete_stmt_btn:
    d.statements.pop(stmt)
    st.rerun()
# two dropdowns side by side
# each containing all the statements
# Three buttons (support, refute and delete)
col1, col2 = st.columns(2)
primary_stmt = col1.selectbox('Select a statement (support)', range(len(d.statements)), format_func=lambda x: d.statements[x])
secondary_stmt = col2.selectbox('Select a statement (refute)', range(len(d.statements)), format_func=lambda x: d.statements[x])

if not secondary_stmt is None and not primary_stmt is None:
    primary_stmt = d.statements[primary_stmt]
    secondary_stmt = d.statements[secondary_stmt]

# Display buttons for support, refute, and delete
support_button = st.button('Support')
refute_button = st.button('Refute')
delete_button = st.button('Delete')

# Handle button actions
if support_button:
    primary_stmt.supports.append(secondary_stmt)
    st.rerun()

if refute_button:
    primary_stmt.refutes.append(secondary_stmt)
    st.rerun()

if delete_button:
    if secondary_stmt in primary_stmt.supports:
        primary_stmt.supports.remove(secondary_stmt)
    if secondary_stmt in primary_stmt.refutes:
        primary_stmt.refutes.remove(secondary_stmt)
    st.rerun()





