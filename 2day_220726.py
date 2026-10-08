##Dictionary Method
# a={"name":"nithish","age":25,"city":"cuddalore","role":"Manager"}
# print(a)
# print(a.items())
# print(a.keys())
# print(a.values())
# print(a.get("age"))
# a.popitem()
# print(a.items())
# a.pop("age")
# print(a.items())

# print(a)
# print(a.items())
# print(a.keys())
# print(a.values())
# print(a.get("name"))
# a.popitem()
# print(a)
# a.pop("city")
# print(a)

# a.update({"mob":94586})
# print(a)
# a["mob"]=6654   #We can alternate the value and the same time we can add the value
# a["height"]=179
# print(a)
# a=("a","b","c","d")
# b=2
# print(dict.fromkeys(a,b))

# a.update({"city2":"simla","role2":"CEO"})
# print(a)
# a["role3"]="MD"
# print(a)
# a["role3"]="supervisor"
# print(a)
#
# c=[1,2,3]
# e={4,5,6}
# f=(3,8,9)
# d=3
# print(dict.fromkeys(c,d))
# print(dict.fromkeys(e,d))
# print(dict.fromkeys(f,d))

##SET Methods
# a={1,2,3,4,5}
# b={3,5,6,6,8}
# c=a.union(b)
# print(c)           ## or print(a.union(b))
# a.update(b)
# print(a)

# c=a.intersection(b)
# print(c)    ##or print(a.difference(b)
# a.intersection_update(b)
# print(a)

# c=a.difference(b)
# print(c)
# a.difference_update(b)
# print(a)


# c=a.symmetric_difference(b)
# print(c)
# c=a.update(b)
# print(c)
# a.intersection_update(b)
# print(a)

# v=a.symmetric_difference(b)
# print(v)

# a={1,2,4}
# c={7,8}
# a.add(5)
# b={1,5}
# print(a)
# print(a)
# a.pop()
# print(a)
# a.remove(7)
# a.remove(5)
# print(a)
# a.discard(4)
# a.discard(7)
# print(a)
# print(b.issubset(a))
# print(a.isdisjoint(b))
# print(a.isdisjoint(c))
# print(c.isdisjoint(a))
# print(max(a))
# a={"name":"nithish","age":25,"city":"cuddalore","role":"Manager"}
# b={"angle":45}
# a.update(b)
# print(a)
# a=[1,2,3,4]
# a[1]="Nithi"
# print(a)
# print(dict.fromkeys(a,b))
# a.append(b)
# print(a)
# a={1,2,3,4,5}
# b={3,32,6}
# print

# fruits=["mango","apple","banana","cherry","pine"]
# print(fruits[0::4])
# fruits.reverse()
# print(fruits)
# fruits.insert(2,"apple")
# fruits.append("orange")
# fruits.remove("apple")
# print(fruits)
# print(fruits.count("apple"))
# fruits.sort()
# print(fruits)
# print(max(fruits))
# print(min(fruits))
# print(list(set(fruits)))
# a=(1,2,3,4,6,7,5,7,4)
# b=(2,6,4,8)
# c=set(a)
# d=set(b)
# print(c.union(d))
# print(c.intersection(d))
# print(c.difference(d))
# print(c.symmetric_difference(d))
# print(d.issubset(c))
# print(c.issuperset(d))
# print(c.isdisjoint(d))
# c.intersection_update(d)
# c.difference_update(d)
# c.update(d)
# print(c)

# a={"name":"nithish","age":23,"city":"USA"}
# print(a.get("name"))
# a["city"]="UK"
# print(a)
# a.pop("city")
# print(a)
# a["course"]="python"
# print(a)
# print(a.keys())
# print(a.values())
# print(a.items())
# c=a.copy()
# print(c)
# print("name" in a)
# print(dict.fromkeys(a,c))
