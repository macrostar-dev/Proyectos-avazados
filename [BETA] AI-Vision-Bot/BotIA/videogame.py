import discord
from discord.ext import commands
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps 
import numpy as np

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Load the model
model = load_model("C:/Users/User/Documents/Kodland/Python Pro/M7L1/BotAI/keras_model.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')



@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f'./{attachment.filename}')
            await ctx.send(f'Guarda la imagen en: ./{attachment.filename}')
            
             # Procesar la imagen con el modelo de Keras
            prediction_result = await process_image(f'./{attachment.filename}')

            # Enviar el resultado al usuario
            await ctx.send(prediction_result)

    else:
        await ctx.send(f'Olvidaste subir la imagen')

async def process_image(image_path):
    try:
        # Abrir y preparar la imagen
        image = Image.open(image_path).convert("RGB")
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        data[0] = normalized_image_array

        # Realizar la predicción con el modelo
        prediction = model.predict(data)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]

        # Definir las categorías y sus respuestas asociadas
        if class_name == "Quemadura1" and confidence_score >= 0.5:
            return f"¡La imagen coincide con una video juego"
        elif class_name == "Quemadura2" and confidence_score >= 0.5:
            return f"¡La imagen coincide con un video juego"
        else:
            return f"La imagen no coincide bien con ninguna imagen."

    except Exception as e:
        return f"Error al procesar la imagen: {str(e)}"

bot.run("TOKEN")
