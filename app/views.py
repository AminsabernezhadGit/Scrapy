# yourappname/views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import multiprocessing

from app.spider.spider.spiders.fetch import DriverFetch


class TriggerSpiderView(APIView):
    def get(self, request, *args, **kwargs):
        # Define a function to run the spider in a separate process
        start_urls = [
            'https://www.digikala.com/product/dkp-8366616/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%A7%D9%BE%D9%84-%D9%85%D8%AF%D9%84-iphone-13-ch-%D8%AF%D9%88-%D8%B3%DB%8C%D9%85-%DA%A9%D8%A7%D8%B1%D8%AA-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-128-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D9%88-%D8%B1%D9%85-4-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D9%86%D8%A7%D8%AA-%D8%A7%DA%A9%D8%AA%DB%8C%D9%88/']
        css_price_selector = 'div.justify-start:nth-child(2) > div:nth-child(1) > span:nth-child(1)'
        css_color_selector = 'div.styles_InfoSectionVariationColor__pX_3M'

        spider_settings = {
            'start_urls': start_urls,
            'css_price_selector': css_price_selector,
            'css_color_selector': css_color_selector,
        }

        def run_spider(settings):
            process = CrawlerProcess(get_project_settings())
            process.crawl(DriverFetch, **settings)
            process.start()
            process.join()

        # Create a multiprocessing Process
        spider_process = multiprocessing.Process(target=run_spider, args=(spider_settings,))

        # Start the process
        spider_process.start()
        spider_process.join()

        return Response({"message": "Spider triggered successfully"}, status=status.HTTP_200_OK)


def home(request):
    return render(request, 'home.html')