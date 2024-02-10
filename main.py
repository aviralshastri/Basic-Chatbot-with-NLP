import flet as ft
import tkinter as tk
from tkinter import PhotoImage, Label, font

import questionprocessor as qp
initial=qp.questionResolver("initial")


def main(page: ft.Page):
    def intializer():
        ContainerBot=ft.Row(spacing=2)
        TextBot=ft.TextField(text_align="LEFT",multiline=True,width=500,value=(initial),color="#1a1a1a",bgcolor="#ffffff",disabled=True,border_radius=20,border_color="#000000")
        IconBot=ft.CircleAvatar(color="#ffffff",bgcolor="#1a1a1a",width=50,height=50,content=ft.Text("BOT"))
        ContainerBot.controls.append(IconBot)
        ContainerBot.controls.append(TextBot)
        chat.controls.append(ContainerBot)
        page.update()

    def buttonClick(e):
        but.disabled=True
        page.update()
        ContainerMe= ft.Row(spacing=2)
        TextMe=ft.TextField(multiline=True,width=500,value=tb.value,color="#ffffff",bgcolor="#1a1a1a",disabled=True,border_radius=20,text_align="RIGHT")
        IconMe=ft.CircleAvatar(color="#1a1a1a",bgcolor="#ffffff",width=50,height=50,content=ft.Text("ME"))
        ContainerMe.controls.append(TextMe)
        ContainerMe.controls.append(IconMe)
        chat.controls.append(ContainerMe)
        ContainerBot=ft.Row(spacing=2)
        TextBot=ft.TextField(text_align="LEFT",multiline=True,width=500,value="Typing...",color="#1a1a1a",text_size=20,bgcolor="#ffffff",disabled=True,border_radius=20,border_color="#000000")
        IconBot=ft.CircleAvatar(color="#ffffff",bgcolor="#1a1a1a",width=50,height=50,content=ft.Text("BOT"))
        ContainerBot.controls.append(IconBot)
        ContainerBot.controls.append(TextBot)
        chat.controls.append(ContainerBot)
        chat.scroll_to(offset=-1, duration=1000)
        meval=tb.value
        tb.value=""
        page.update()
        answer=qp.questionResolver(meval)
        TextBot.value=answer
        TextBot.text_size=16
        but.disabled=False
        chat.scroll_to(offset=-1, duration=1000)
        page.update()
    
    page.window_width=600
    page.window_height=700
    page.window_resizable=False
    page.window_maximizable=False
    chat=ft.ListView(expand=True,spacing=5,width=580)
    chatContainer=ft.Container(
        content=chat,
        bgcolor="#d9d9d9",
        padding=5,expand=True,
        border_radius=10,
    )
    tb = ft.TextField(
        label="Message",
        width=480,border_radius=30
    )
    but=ft.IconButton(on_click=buttonClick,icon=ft.icons.SEND,
                    icon_color="black",icon_size=50,width=80)
    MessageInputContainer = ft.Row(spacing=8,controls=[tb,but])
    page.add(chatContainer,MessageInputContainer)
    intializer()
    

ft.app(target=main,name="ChatBot")