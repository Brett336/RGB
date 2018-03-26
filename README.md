# RGB_IR_Bulb


Working But incomplete project due to not having the time to complete it.


The ardunino is programmed to send Hex codes received over serial over the NEC IR Protocol. This means any hex code for any light bulb using the NEC protocol can be used to control the light in question. 

The Python servers store the hex code for my specific brand of bulb (https://www.amazon.co.uk/gp/product/B00CSTU7C2/ref=oh_aui_detailpage_o09_s00?ie=UTF8&psc=1)
however in the future I plan to add options to add custom codes and remove the defualt ones.
It can also be used to control IR RGB lighing strips or anything that uses the NEC protocol. This could potentialy be used to control multiple lights at once.

The python server also can be used to program certain lighting effects such as flashing between two differnt colors by sending the hex codes repeatedly to the arduino, simulating the remote being pressed quickly. 

