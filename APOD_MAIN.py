#!/usr/bin/python3
from tkinter import *
from tkinter.ttk import OptionMenu, Button, Checkbutton
from tkinter import messagebox
import tkinter as tk

from APOD_VIEW import ApodView
from APOD_CONTROLLER import ApodController


class ApodMain:

    apod_controller = ApodController()
    apod_view = ApodView()
    apod_controller.set_view(apod_view)
    apod_view.init_window(apod_controller)