#!/usr/bin/env python
#
#       Ferit Yiğit BALABAN, <fybalaban@fybx.dev>
#
#       engine.py
import memory
import parser
import processor


class Engine:
    def __init__(self):
        self.__cpu = processor.Processor()
        self.__ram = memory.Memory()
        self.__parser = parser.Parser()
        self.__delay = 1

    def load_source_code(self, source_code: str):
        self.__parser.parse_code(source_code)
        self.__parser.load_to_memory(self.__ram)

    def set_frequency(self, frequency: float):
        """
        Çalıştırma motorunun her işlem arasına getirdiği gecikmeyi milisaniye cinsinden ayarlar.
        Gecikme (ms) = 1000 / frequency
        :param frequency: Saniye başına satır çalıştırma hızı
        """
        self.__delay = 1000 / frequency

