# Week4-Switch-HW

The Library Exercise and The Permutations Exercise

Option A: Using Three Dictionaries
Description: - One dictionary stores books by their IDs. - The second maps titles to book IDs. - The third maps authors to lists of book IDs.

    Pros:
    - Efficient search by title or author (O(1) for dictionary lookups).
    - Allows easy updates and removals without duplicating data.
    - Scales well for large data sets due to the efficient hashing mechanism.

    Cons:
    - Increased complexity due to maintaining multiple dictionaries.
    - Risk of inconsistency if changes aren’t synchronized across dictionaries.

Option B: Using a List of Book Objects
Description: - A single list contains objects, where each object represents a book with all its attributes.

    Pros:
    - Simple and easy to implement.
    - No risk of synchronization issues since data is centralized in one structure.
    - Flexible for adding more attributes to books.

    Cons:
    - Searching requires iterating through the list (O(n) complexity), which can become slow for large libraries.
    - Less efficient for operations targeting specific fields (e.g., search by author).
