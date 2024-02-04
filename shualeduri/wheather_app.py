import sys
import requests
from PyQt5.QtGui import QMovie, QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QComboBox


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Weather App')
        self.setGeometry(100, 100, 400, 200)
        # self.setStyleSheet("background: #ff7e5f;")

        self.layout = QVBoxLayout()

        self.background_label = QLabel(self)
        self.background_label.setFixedWidth(400)
        self.background_label.setFixedHeight(225)
        self.movie = QMovie("default_animation.gif")
        self.background_label.setMovie(self.movie)
        self.movie.start()

        self.city_label = QLabel('Select city:')
        self.city_combobox = QComboBox()
        self.city_combobox.addItems(
            ['Tbilisi, Georgia', 'Barrow, Alaska', 'Riyadh, Saudi Arabia', 'Sydney, Australia', 'Tromsø, Norway',
             'Mexico City, Mexico',
             'Mumbai, India', 'Reykjavik, Iceland', 'Nairobi, Kenya', 'Ushuaia, Argentina', 'Cairo, Egypt',
             'Vancouver, Canada', 'Nuuk, Greenland', 'Dubai, United Arab Emirates', 'Rio de Janeiro, Brazil',
             'Tokyo, Japan', 'Anchorage, Alaska', 'Auckland, New Zealand', 'Moscow, Russia',
             'Singapore, Singapore',
             'Bergen, Norway', 'Phoenix, Arizona', 'Cape Town, South Africa', 'Oslo, Norway', 'Bangkok, Thailand',
             'Montreal, Canada', 'Buenos Aires, Argentina', 'Stockholm, Sweden', 'Lima, Peru', 'Seoul, South Korea',
             'Honolulu, Hawaii'])
        self.search_button = QPushButton('Search')
        self.result_label = QLabel('')
        self.result_label_1 = QLabel('')

        self.search_button.clicked.connect(self.get_weather)

        self.layout.addWidget(self.background_label)
        self.layout.addWidget(self.city_label)
        self.layout.addWidget(self.city_combobox)
        self.layout.addWidget(self.search_button)
        self.layout.addWidget(self.result_label_1)
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

    def get_weather(self):
        city = self.city_combobox.currentText()

        if not city:
            QMessageBox.warning(self, 'Error', 'Please enter a city name')
            return

        api_key = '045e01d58ee218d1ae37cead2c9728b3'
        base_url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'appid': api_key,
                  'units': 'metric'}

        try:
            response = requests.get(base_url, params=params)
            data = response.json()
            print(response)
            print(data)

            if response.status_code == 200:
                icon_code = data['weather'][0]['icon']
                icon_url = f'http://openweathermap.org/img/w/{icon_code}.png'
                response = requests.get(icon_url, stream=True)
                if response.status_code == 200:
                    with open(f'{icon_code}.png', 'wb') as f:
                        for chunk in response.iter_content(1024):
                            f.write(chunk)

                    self.result_label_1.setText(f'<img src="{icon_code}.png" height="60" width="60"> hello')
                else:
                    QMessageBox.warning(self, 'Error', f'Icon download failed: {response.status_code}')

                temperature = data['main']['temp']
                description = data['weather'][0]['description']
                humidity = data['main']['humidity']
                wind_speed = data['wind']['speed']
                country = data['sys']['country']
                city_name = data['name']

                gif_filename = self.get_background_gif(description.lower())
                self.set_background_gif(gif_filename[0])

                result_text = (
                    f'City: {city_name}, {country}\n'
                    f'Temperature: {temperature}°C\n'
                    f'Description: {description}\n'
                    f'Humidity: {humidity}%\n'
                    f'Wind Speed: {wind_speed} m/s'
                )
                self.result_label.setText(result_text)


            else:
                message = data.get('message', 'Unknown error')
                QMessageBox.warning(self, 'Error', f'Error: {message}')

        except requests.RequestException as e:
            QMessageBox.warning(self, 'Error', f'Request error: {e}')

    @staticmethod
    def get_background_gif(weather_description):
        if 'clear' in weather_description:
            return ['sky_blue.gif', 'clear.gif']
        elif 'cloud' in weather_description:
            return ['cloudy.gif', 'file.gif']
        elif 'rain' in weather_description:
            return ['rain.gif', 'file.gif']
        elif 'mist' in weather_description:
            return ['mist.gif', 'file.gif']
        elif 'snow' in weather_description:
            return ['snow.gif', 'file.gif']
        else:
            return ['default_animation.gif', 'clear.gif']

    def set_background_gif(self, gif_filename):
        self.movie.stop()
        self.movie.setFileName(gif_filename)
        self.movie.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
