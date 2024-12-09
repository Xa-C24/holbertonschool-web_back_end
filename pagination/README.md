# Pagination in Python

## **Introduction**
Pagination is a technique used to divide large datasets into smaller, manageable parts called **pages**. It enhances the user experience, optimizes resource usage, and improves application performance by avoiding the need to load all data at once.

---

## **Why Use Pagination?**

### **Advantages**
1. **Performance Optimization:**
   - Prevents server overload.
   - Reduces memory usage.
2. **Improved User Experience:**
   - Simplifies navigation through large datasets.
   - Presents data in digestible chunks.
3. **Scalability:**
   - Makes handling large datasets feasible.

---

## **Types of Pagination**

### 1. **Basic Pagination**
- Uses simple parameters like `page` and `page_size` to navigate data.
- Example API Call:
  ```
  GET /data?page=2&page_size=10
  ```

### 2. **Hypermedia Pagination**
- Includes additional metadata in responses, such as:
  - **Page Size:** Number of items per page.
  - **Current Page:** Current page number.
  - **Next Page / Previous Page:** Links to navigate.
  - **Total Pages:** Total number of pages.
- Example Response:
  ```json
  {
    "page_size": 10,
    "page": 2,
    "data": [...],
    "next_page": 3,
    "prev_page": 1,
    "total_pages": 50
  }
  ```

### 3. **Deletion-Resilient Pagination**
- Ensures no data is skipped if rows are deleted between user requests.
- Relies on indexing datasets to maintain consistent access.

---

## **Implementation in Python**

### **Helper Function**
The `index_range` function calculates start and end indices for a given page and page size.
```python
# Helper Function

def index_range(page: int, page_size: int):
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
```

### **Server Class**
The `Server` class demonstrates a simple pagination system for a dataset stored in a CSV file.
```python
import csv
from typing import List

class Server:
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                self.__dataset = [row for row in reader][1:]  # Skip header
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]
```

### **Hypermedia Metadata**
Adds metadata to the response for enhanced navigation.
```python
def get_hyper(self, page: int = 1, page_size: int = 10):
    data = self.get_page(page, page_size)
    total_pages = math.ceil(len(self.dataset()) / page_size)
    return {
        "page_size": len(data),
        "page": page,
        "data": data,
        "next_page": page + 1 if page < total_pages else None,
        "prev_page": page - 1 if page > 1 else None,
        "total_pages": total_pages
    }
```

### **Deletion-Resilient Pagination**
Maintains access consistency even after deletions.
```python
def get_hyper_index(self, index: int, page_size: int = 10):
    assert index >= 0 and index < len(self.indexed_dataset())
    data = []
    next_index = index
    for _ in range(page_size):
        while next_index not in self.indexed_dataset():
            next_index += 1
        data.append(self.indexed_dataset()[next_index])
        next_index += 1
    return {
        "index": index,
        "data": data,
        "page_size": len(data),
        "next_index": next_index
    }
```

---

## **Key Considerations**
1. **Input Validation:**
   - Ensure `page` and `page_size` are positive integers.
2. **Error Handling:**
   - Return an empty list if the indices are out of range.
3. **Efficiency:**
   - Cache datasets for faster access.

---

## **Use Cases**
1. **Web Applications:**
   - Blogs or e-commerce sites displaying limited items per page.
2. **APIs:**
   - REST APIs with large datasets.
3. **Data Analysis:**
   - Interactive tools handling large datasets.

---

## **Resources**
- [REST API Design: Pagination](https://restfulapi.net/pagination/)
- [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS)

---

By following this guide, you can effectively implement and understand pagination for various applications.

