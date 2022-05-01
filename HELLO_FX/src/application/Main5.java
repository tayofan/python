package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.stage.Stage;


public class Main5 extends Application {
	Button btn;
	TextField tf_dan;
	TextArea ta_dan;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			Parent root = FXMLLoader.load(getClass().getResource("main5.fxml"));
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			tf_dan = (TextField) scene.lookup("#tf_dan");
			ta_dan = (TextArea) scene.lookup("#ta_dan");
			btn = (Button) scene.lookup("#btn");
			btn.setOnMouseClicked(new EventHandler<Event>() {

				@Override
				public void handle(Event event) {
					printDan();
					
				}
				
			});
			
			primaryStage.setScene(scene);
			primaryStage.show();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public void printDan() {
		String output = "";
		try {
			int dan = Integer.parseInt(tf_dan.getText());
			output += dan + " * " + 1 + " = " + dan*1 + "\n";
			output += dan + " * " + 2 + " = " + dan*2 + "\n";
			output += dan + " * " + 3 + " = " + dan*3 + "\n";
			output += dan + " * " + 4 + " = " + dan*4 + "\n";
			output += dan + " * " + 5 + " = " + dan*5 + "\n";
			output += dan + " * " + 6 + " = " + dan*6 + "\n";
			output += dan + " * " + 7 + " = " + dan*7 + "\n";
			output += dan + " * " + 8 + " = " + dan*8 + "\n";
			output += dan + " * " + 9 + " = " + dan*9 + "\n";
		} catch (Exception e) {
			output += "단을 입력해주세요";
		}
		ta_dan.setText(output);
		
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
