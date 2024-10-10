package j;

import javafx.beans.property.*;

public class Book {
    private final IntegerProperty id;
    private final StringProperty title;
    private final StringProperty author;
    private final StringProperty isbn;
    private final StringProperty available;

    public Book(int id, String title, String author, String isbn, int available) {
        this.id = new SimpleIntegerProperty(id);
        this.title = new SimpleStringProperty(title);
        this.author = new SimpleStringProperty(author);
        this.isbn = new SimpleStringProperty(isbn);
        this.available = new SimpleStringProperty(available == 1 ? "Yes" : "No");
    }

    // Getters and setters
    public int getId() { return id.get(); }
    public IntegerProperty idProperty() { return id; }

    public String getTitle() { return title.get(); }
    public StringProperty titleProperty() { return title; }

    public String getAuthor() { return author.get(); }
    public StringProperty authorProperty() { return author; }

    public String getIsbn() { return isbn.get(); }
    public StringProperty isbnProperty() { return isbn; }

    public String getAvailable() { return available.get(); }
    public StringProperty availableProperty() { return available; }
}
