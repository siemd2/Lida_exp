import streamlit as st
from lida import Manager, TextGeneration, llm
from dotenv import load_dotenv
import os
import openai
import io
from PIL import Image
from io import BytesIO
import base64
