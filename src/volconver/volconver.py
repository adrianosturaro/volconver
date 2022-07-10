from typing import Dict
from typing_extensions import Protocol
from pkg_resources import iter_entry_points


class Converter(Protocol):
    produto: str

    def dens20(self, temp_amostra: float, den_amostr: float) -> float:
        ...

    def fator(self, temp_amostra: float, den_amostr: float, temp_ct: float) -> float:
        ...


class VolumeConverter:
    def __init__(self):
        self.converters: Dict[str, Converter] = {}

    def registra_converter(self):
        self.converters = {
            emp.name: emp.load()() for emp in iter_entry_points(group="volconverplugin")
        }


def main():
    volconverter = VolumeConverter()
    volconverter.registra_converter()
    den = volconverter.converters["Derivados"].dens20(20, 0.8)
    print(den)


if __name__ == "__main__":
    main()
