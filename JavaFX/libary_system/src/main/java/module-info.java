module j {
    requires javafx.controls;
    requires javafx.fxml;
    requires java.sql;

    opens j to javafx.fxml;
    exports j;
}
