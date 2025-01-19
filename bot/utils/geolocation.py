import aiohttp
import random

from bot.utils.logger import logger
from geopy.distance import geodesic
from geopy import Point
from aiohttp_proxy import ProxyConnector
from aiohttp import TCPConnector
from typing import Optional, Tuple

class Geo:
    def __init__(self, proxy=None):
        self.proxy = proxy

        self.proxy_connector = ProxyConnector().from_url(self.proxy) if self.proxy else TCPConnector(verify_ssl=False)
        self.session = aiohttp.ClientSession(connector=self.proxy_connector, trust_env=True)

    @staticmethod
    async def generate_random_location(center: Point, radius_km: float = 100) -> Tuple[float, float]:
        random_angle = random.uniform(0, 360)  # случайный угол
        random_distance = random.uniform(0, radius_km)  # случайное расстояние в километрах
        destination_point = geodesic(kilometers=random_distance).destination(center, random_angle)
        return destination_point.latitude, destination_point.longitude

    async def get_info_from_proxy(self) -> Optional[Tuple[float, float, str, str]]:
        response = await self.session.get(url='http://ip-api.com/json', timeout=aiohttp.ClientTimeout(20))
        response.raise_for_status()
        if response.status == 200:
            response_json = await response.json()
            lat = response_json.get("lat")
            lon = response_json.get("lon")
            city_coordinates = Point(lat, lon)
            random_lat, random_lon = await self.generate_random_location(city_coordinates, radius_km=50)

            countryCode = response_json.get("countryCode")
            locale = f"en-{countryCode}"
            timezone = response_json.get("timezone")
            return random_lat, random_lon, locale, timezone

        else:
            logger.error(f"Не удалось получить страну прокси: {self.proxy}")
            return None

    async def close_connection(self):
        await self.session.close()

