from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import RPi.GPIO as GPIO

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Led Pinout
livingroom = 27
big_bedroom = 17
small_bedroom = 18
bathroom = 22
kitchen = 23
outside = 24

# Switch Pinout
livingroom_button = 21
big_bedroom_button = 20
small_bedroom_button = 26
bathroom_button = 16
kitchen_button = 19
outside_button = 13

# Gate Pinout
gate_led = 4
gate_button = 25
gate_closed = 6
gate_opened = 12

# Sensor Pinout
light = 5

# GPIO Header
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(light, GPIO.IN)

GPIO.setup(gate_button, GPIO.IN)
GPIO.setup(gate_led, GPIO.OUT)
GPIO.setup(gate_closed, GPIO.IN)
GPIO.setup(gate_opened, GPIO.IN)

GPIO.setup(livingroom, GPIO.OUT)
GPIO.setup(big_bedroom, GPIO.OUT)
GPIO.setup(small_bedroom, GPIO.OUT)
GPIO.setup(bathroom, GPIO.OUT)
GPIO.setup(kitchen, GPIO.OUT)
GPIO.setup(outside, GPIO.OUT)

GPIO.setup(livingroom_button, GPIO.IN)
GPIO.setup(big_bedroom_button, GPIO.IN)
GPIO.setup(small_bedroom_button, GPIO.IN)
GPIO.setup(bathroom_button, GPIO.IN)
GPIO.setup(kitchen_button, GPIO.IN)
GPIO.setup(outside_button, GPIO.IN)

# Changestate function
def changestate(pin):
    if GPIO.input(pin) == True:
        GPIO.output(pin, False)
    else:
        GPIO.output(pin, True)

# Lights functions
def livingroom(update: Update, _: CallbackContext) -> None:
    changestate(livingroom)
    update.message.reply_text("Done")


def big_bedroom(update: Update, _: CallbackContext) -> None:
    changestate(big_bedroom)
    update.message.reply_text("Done")


def small_bedroom(update: Update, _: CallbackContext) -> None:
    changestate(small_bedroom)
    update.message.reply_text("Done")


def outside(update: Update, _: CallbackContext) -> None:
    changestate(outside)
    update.message.reply_text("Done")


def kitchen(update: Update, _: CallbackContext) -> None:
    changestate(kitchen)
    update.message.reply_text("Done")


def bathroom(update: Update, _: CallbackContext) -> None:
    changestate(bathroom)
    update.message.reply_text("Done")


# Gate command
def gate(update: Update, _: CallbackContext) -> None:
    print("La funzione avrebbe bisogno dei thread. Non è acnora stata sviluppata.")
    update.message.reply_text("Il cancello non funziona")
        

# Entry commands
def start(update: Update, _: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Ciao {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, _: CallbackContext) -> None:
    update.message.reply_text('Per accendere una luce usa /"nome della stanza" per esempio /salotto')


# Echo command
def echo(update: Update, _: CallbackContext) -> None:
    update.message.reply_text("Il bot non supporta ancora i messaggi normali. Utilizza i comandi con /comando")


def main() -> None:
    """Start the bot."""
    updater = Updater("1752829650:AAFUppicxpijbKmDfw9cduuM7GlufTpDIMs")
    dispatcher = updater.dispatcher

    # Entry commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Room commands
    dispatcher.add_handler(CommandHandler("salotto", livingroom))
    dispatcher.add_handler(CommandHandler("camera", big_bedroom))
    dispatcher.add_handler(CommandHandler("cameretta", small_bedroom))
    dispatcher.add_handler(CommandHandler("bagno", bathroom))
    dispatcher.add_handler(CommandHandler("cucina", kitchen))
    dispatcher.add_handler(CommandHandler("esterno", outside))

    # Gate command
    dispatcher.add_handler(CommandHandler("cancello", gate))

    # Echo command
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
