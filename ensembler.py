from ultralytics import YOLO
from PIL import Image

infrared_model = YOLO('models/infrared.pt')
visible_model = YOLO('models/visible.pt')
thermal_model = YOLO('models/thermal.pt')

infrared_img = Image.open("images/infrared.jpg")
visible_img = Image.open("images/visible.jpg")
thermal_img = Image.open("images/thermal.jpg")


results_infrared = infrared_model.predict(source=infrared_img, save=True)
results_visible = visible_model.predict(source=visible_img, save=True)
results_thermal = thermal_model.predict(source=thermal_img, save=True)






