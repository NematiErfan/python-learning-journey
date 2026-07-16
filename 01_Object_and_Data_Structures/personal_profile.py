# ============================================
"""
Project 01 - Personal Profile Manager

This project demonstrates basic Python data structures including:
- Variables
- Strings
- Numbers
- Lists
- Dictionaries
- Tuples
- Sets

Author: Erfan Nemati
"""
# ============================================


personal_info = {'Name':'Erfan Nemati', 'Age': 35, 'Country':'Iran', 'Height(m)': 1.8, 'Goals':['Python','Git', 'FPGA', 'Linux']}
programming_languages_list = ['Python', 'VHDL', 'Verilog']
goals_tuple = ('Study in Germany', 'Become an AI Engineer', 'Build AI Product')
tec_learning_list = ['FPGA', 'Python', 'DSP', 'Microblaze', 'Interface', 'FPGA', 'FPGA', 'Python', 'DSP']


print('=========================')
print('Personal Profile Report')
print('=========================')
print('Name:' , personal_info['Name'])
print('Age:' , personal_info['Age'])
print('Country:' , personal_info['Country'])
print('Height:' , personal_info['Height(m)'])
print()
print('programming Languages:' , programming_languages_list)
print()
print('Future Goals:' , goals_tuple)
print()
learning_technologies = set(tec_learning_list)
print('Technologies:' , learning_technologies)
print()
print('=========================')