import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


@pytest.mark.skip("TODO")
def test_hash():
    """
    NOTE: intentionally breaks "encapsulation" by accessing "internal" attriubutes
    """
    hashtable = Hashtable()
    actual = hashtable._hash("Zach")
    assert 0 <= actual < hashtable._size


@pytest.mark.skip("TODO")
def test_hash_twice():
    """
    NOTE: intentionally breaks "encapsulation" by accessing "internal" attriubutes
    """
    hashtable = Hashtable()
    first = hashtable._hash("Zach")
    second = hashtable._hash("Zach")
    assert first == second


@pytest.mark.skip("TODO")
def test_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_apple_again():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("apple", "Can give to teacher")
    actual = hashtable.get("apple")
    expected = "Can give to teacher"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_key_not_exists():
    hashtable = Hashtable()
    actual = hashtable.get("nonexisting key")
    expected = None
    assert actual == expected


@pytest.mark.skip("TODO")
def test_key_not_exists_again():
    """
    WARNING: requires that act & cat hash the same
    """
    hashtable = Hashtable()
    hashtable.set("cat", "meow")
    actual = hashtable.get("act")
    expected = None
    assert actual == expected


@pytest.mark.skip("TODO")
def test_keys():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("banana", "Great in a banana split")
    actual = hashtable.keys()
    expected = ["apple", "banana"]
    assert sorted(actual) == sorted(expected)


@pytest.mark.skip("TODO")
def test_has():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("banana", "Great in a banana split")
    assert hashtable.has("apple")
    assert hashtable.has("banana")
    assert not hashtable.has("cucumber")


@pytest.mark.skip("TODO")
def test_keys_repeats():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("apple", "Can give to teacher")
    hashtable.set("banana", "Great in a banana split")
    actual = hashtable.keys()
    expected = ["apple", "banana"]
    assert sorted(actual) == sorted(expected)


@pytest.mark.skip("TODO")
def test_internals():
    """
    NOTE: there's a test_internals in your DSA repo that isn't a great fit.
    Feel free to ignore it
    Or tweak it as a STRETCH
    """
    pass
