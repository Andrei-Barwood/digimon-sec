# Guía de Uso - Ciphermon (Mega)

## Instalación rápida
```bash
pip install -e .
```

## Ejemplos

### Evaluar política
```python
from ciphermon import Ciphermon

digimon = Ciphermon()
res = digimon.analyze(cipher="AES-256-GCM", key_bits=256, aead=True)
print(res)
```

### Cifrado simulado + integridad
```python
from ciphermon import Ciphermon

digimon = Ciphermon()
enc = digimon.encrypt("hola digimundo")
print(enc)
dec = digimon.decrypt(enc.data["ciphertext"], enc.data["key"])
print(dec)
```

### Política con alerta legacy
```python
from ciphermon import Ciphermon

digimon = Ciphermon()
res = digimon.analyze(cipher="AES-128-CBC", key_bits=128, aead=False)
print(res)
```

Ver también: [API.md](API.md), [ARCHITECTURE.md](ARCHITECTURE.md)
# Guía de Uso - ciphermon

## Inicio Rápido

### Instalación

```bash
pip install -e .
```

### Uso Básico

```python
from ciphermon.core import Ciphermon

digimon = Ciphermon()
result = digimon.analyze()
print(result)
```

---

Ver también: [ARCHITECTURE.md](ARCHITECTURE.md), [API.md](API.md)
