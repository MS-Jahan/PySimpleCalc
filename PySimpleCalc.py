#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  PySimpleCalc.py
#  
#  Copyright 2019 Md Sarwar Jahan Sabit <ssarwarjahan@gmail.com>
#  
#  This program is free software; you can redistribute it and/or button is modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or button is
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or button is FITNESS For button is A PARTICULAR PURPOSE.  See the
#  GNU General Public License for button is mor button ise details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor button is, Boston,
#  MA 02110-1301, USA.
#  
#  

import PySimpleGUI as sg

image_del = './ButtonGraphics/del.png'

layout = [[sg.Text('PySimpleCalc', justification='center', font='any 20')],
          [sg.Text('A Simple Calculator, Made With PySimpleGUI.')],
          [sg.Text('Display: '), sg.InputText('', key='disp', size=(14,1)), sg.Button('', image_filename=image_del, button_color=('#d9d9d9', '#d9d9d9'), image_size=(37, 26), image_subsample=25, border_width=0, key='del')],
          [sg.RButton('7', button_color=('black', 'white')), sg.RButton('8', button_color=('black', 'white')), sg.RButton('9', button_color=('black', 'white')), sg.RButton('/', size=(1,1), button_color=('black', '#4a90d9'))],
          [sg.RButton('4', button_color=('black', 'white')), sg.RButton('5', button_color=('black', 'white')), sg.RButton('6', button_color=('black', 'white')), sg.RButton('*', size=(1,1), button_color=('black', '#4a90d9'))],
          [sg.RButton('1', button_color=('black', 'white')), sg.RButton('2', button_color=('black', 'white')), sg.RButton('3', button_color=('black', 'white')), sg.RButton('-', size=(1,1), button_color=('black', '#4a90d9'))],
          [sg.RButton('AC', size=(1,1), button_color=('white', 'red')), sg.RButton('0', button_color=('black', 'white')), sg.RButton('.', size=(1,1), button_color=('white', 'red')), sg.RButton('+', size=(1,1), button_color=('black', '#4a90d9')), sg.RButton('=', size=(1,1), button_color=('white', 'springgreen4'))]
          ]
          
window = sg.Window('PySimpleGUI').Layout(layout)

first_number = None
last_number = None


def add(a, b):
	add_answer = a + b
	return add_answer
	
def minus(a, b):
	minus_answer = a - b
	return minus_answer
	
def mult(a, b):
	mult_answer = a * b
	return mult_answer
	
def devide(a, b):
	devide_answer = a / b
	return devide_answer
	
status = None	
	
while True:
	button, values = window.Read()
    
    
    
	if button is None:
		break
	
	if button is 'del':
			values['disp'] = values['disp'][:-1]
			window.FindElement('disp').Update(values['disp'])
	
	if (button is '1') or (button is '2') or (button is '3') or (button is '4') or (button is '5') or (button is '6') or (button is '7') or (button is '8') or (button is '9') or (button is '0') or (button is '.'):
		values['disp'] = str(values['disp']) + str(button)
		window.FindElement('disp').Update(values['disp'])
		
	'''if (button is not '1') or (button is not '2') or (button is not '3') or (button is not '4') or (button is not '5') or (button is not '6') or (button is not '7') or (button is not '8') or (button is not '9') or (button is not '0') or (button is not '=') or (button is not 'AC') or (button is not '.'):
	'''	
		
	if button == '+':
		values['disp'] = values['disp'].replace('+','')
		print(values['disp'])
		first_number = float(values['disp'])
		values['disp'] = ''
		button, values = window.Read()
		window.FindElement('disp').Update(values['disp'])
		values['disp'] = button
		window.FindElement('disp').Update(values['disp'])
		status = '+'
		
		
	
	elif button == '-':
		values['disp'] = values['disp'].replace('-','')
		print(values['disp'])
		first_number = float(values['disp'])
		values['disp'] = ''
		button, values = window.Read()
		window.FindElement('disp').Update(values['disp'])
		values['disp'] = button
		window.FindElement('disp').Update(values['disp'])
		status = '-'
		
	
	elif button == '*':
		values['disp'] = values['disp'].replace('*','')
		print(values['disp'])
		first_number = float(values['disp'])
		values['disp'] = ''
		button, values = window.Read()
		window.FindElement('disp').Update(values['disp'])
		values['disp'] = button
		window.FindElement('disp').Update(values['disp'])
		status = '*'
		
	
	elif button == '/':
		values['disp'] = values['disp'].replace('/','')
		print(values['disp'])
		first_number = float(values['disp'])
		values['disp'] = ''
		button, values = window.Read()
		window.FindElement('disp').Update(values['disp'])
		values['disp'] = button
		window.FindElement('disp').Update(values['disp'])
		status = '/'
		

	
	if button == '=' and status == '+' and values['disp'] != '':
		last_number = float(values['disp'])
		equal = add(first_number, last_number)
		values['disp'] = equal
		window.FindElement('disp').Update(values['disp'])
		first_number = equal
	elif button == '=' and status == '-':
		last_number = float(values['disp'])
		equal = minus(first_number, last_number)
		values['disp'] = equal
		window.FindElement('disp').Update(values['disp'])
		first_number = equal
	elif button == '=' and status == '*':
		last_number = float(values['disp'])
		equal = mult(first_number, last_number)
		values['disp'] = equal
		window.FindElement('disp').Update(values['disp'])
		first_number = equal
	elif button == '=' and status == '/':
		last_number = float(values['disp'])
		equal = devide(first_number, last_number)
		values['disp'] = equal
		window.FindElement('disp').Update(values['disp'])
		first_number = equal
	elif button == '=' and status == None:
		sg.PopupOK('                              Enter valid numbers first!                         ', title='NOT TOO FAST, DUDE!')
	elif button == '=' and values['disp'] == '':
		sg.PopupOK('                              Enter valid numbers first!                         ', title='NOT TOO FAST, DUDE!')
	
			
	if button == 'AC':
		values['disp'] = ''
		status = None
		first_number = None
		last_number = None
		window.FindElement('disp').Update(values['disp'])			
								

		
