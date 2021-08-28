# AAaaS

Ascii-Art as a Service is a service which provides you with ascii art on demand. Simply enter a "search" and ascii art will be provided from a random image matching that search.

### Api
You can also use the api:

```python
import requests

width = 100
mode = "ascii"
search = ""

print(requests.get(f"http://aaaas.art/api?width={width}&mode={mode}&s={search}"))
```