import random, webbrowser 
for _ in range(15):
    webbrowser.open(f"https://mylicence.sa.gov.au/hazard-perception-test/{random.randint(1, 5)}/{random.randint(1, 7)}")