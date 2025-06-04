"""
Example usage of the RefCatch package.
"""

from refcatch import refcatch

def main():
    """Run a simple example of RefCatch."""
    print("RefCatch Example")
    print("---------------")
    
    # Define input and output files
    input_file = "refs.md"
    output_file = "refs_with_dois.md"
    doi_file = "dois.txt"
    
    print(f"Processing references from {input_file}...")
    
    # Run RefCatch
    success, message, doi_count = refcatch(
        input_file=input_file,
        output_file=output_file,
        doi_file=doi_file,
        log=True
    )
    
    if success:
        print("\nSuccess!")
    else:
        print("\nFailed.")
    
    print(message)

if __name__ == "__main__":
    main()
