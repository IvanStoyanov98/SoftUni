class Band:

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album not in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."
        return f"Band {self.name} already has {album.name} in their library."

    def remove_album(self, album_name):
        for album in self.albums:
            if album.name == album_name:
                if album.published:
                    return "Album has been published. It cannot be removed."
                self.albums.remove(album)
                return f"Album {album.name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        result = f"Band {self.name}\n"
        for album in self.albums:
            result += f"{album.details()}\n"

        return result.strip()