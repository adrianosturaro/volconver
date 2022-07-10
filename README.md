# volconver

<p style="text-align: justify">Este pacote  é usado para converssão de volume de derivados de petróleo e tem propósito academico, não deve ser usados para converssões reais.</p>


## Instalação

---

Execute o seguinte para instalar:

```python
pip install volconver
```

## Uso

---
```python
from volconver import VolConverter

der_conv = VolConverter("Derivados")
dens20 =  der_conv.dens20(temp_amostra=32.3, dens_amostra=0.8234)
```
## Desenvolvimento
---

<p style="text-align: justify">Para instalar vvolconver junto com as ferramentas para desenvolver e realizar testes,
use o seguinte comando:</p>

```python
pip install -e .[dev]
```