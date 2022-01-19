def cubiod(l, w, h):
    if l <= 0 or w <= 0 or h <= 0:
        print("not a cubiod, edge should not be 0")
        return "not a cubiod, edge should not be 0"
    else:
        volume = l*w*h 
        print (volume)
        surfaceArea = 2*((w*l) + (l*h) + (h*w))
        print (surfaceArea)
        sumOfEdges = l+w+h
        print(sumOfEdges)
        print({"volume": volume,
                "surface area": surfaceArea,
                "sum of edges": sumOfEdges})
        return {"volume": volume,
                "surface area": surfaceArea,
                "sum of edges": sumOfEdges}

cubiod(10, 5, 10)
cubiod(5.5, 5, 10)
cubiod(-5, 5, 10)
cubiod(a, 5, 5)