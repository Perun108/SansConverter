# SansConverter
A converter for different Sanskrit transliteration systems

SansConverter is an offline program that allows you to easily and quickly convert transliterated Sanskrit text from one transliteration system to another. You can also type in Sanskrit text in the standard Roman transliteration (IAST) (or other systems) using just your standard QWERTY keyboard.

You can use it to create Sanskrit text with diacritics to use it later in online posts, messages, books, articles, etc.  

SansConverter features:

- Several well-known systems are supported, namely Balaram (1), IAST (2), Harvard-Kyoto (3), Velthuis (4), Cyrillic transliteration both in Russian (5) and Ukrainian (6) versions.
- The text is converted “on the spot” while you are typing or whenever it is pasted into the input window. 
- The program remembers previous transliteration systems that you chose last time and opens them automatically when started next time.
- It also remembers the size of the window (if you resize it) and its position (if you move it on your screen). 
- You can also access all buttons and select transliteration systems with your keyboard, either by pressing Tab or using the shortcuts (Note for Mac OS X users – to use navigation with Tab you first have to go to “System Preferences” and then go to “Keyboard Preferences” and click on Shortcuts” tab and them go to “Accessibility” section and select “all controls” under “Full keyboard access”). 
- You can choose between “ṁ” or “ṃ” by checking the box in the main window (this setting is also remembered at next start).
- Text can be pasted from the clipboard and converted text can be copied to clipboard by pressing the respective buttons. 

NOTE: 
There is a bug when converting from IAST to Balaram which is caused by the way Balaram system was build - “ṣ” is converted to “ñ”. Thus if you convert IAST text like “puruṣa” to Balaram you will get “puruïa” (“puruña”). This is because “ñ” was also used in Balaram and thus it gets converted wrongly. Since Balaram is a legacy system and I don’t know if many people will use this program to convert IAST text to Balaram I decided to save time and to leave this as it is for now. The workaround for such little problem is to first convert from IAST to any other system (preferably Velthuis because it allows capital letters) and then use “Swap transliterations and texts” button and selecting Balaram as a target transliteration. 

INSTALLATION:
The program requires no installation and you can just drag and drop the .exe or .app file to your Panel in Windows or to your Application folder or Dock on Mac. However, if you want to install it as a regular application on your Windows system you can use the installer “SansConverter_v1.0_Install.exe”.

There is some more information about transliteration systems under “Help” menu. 

You can also send your feedback or reports to the address given in the “About” menu. 
