package application;
	
import java.io.IOException;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.PopupControl;
import javafx.scene.control.TextField;
import javafx.stage.Popup;
import javafx.stage.Stage;


public class Main8 extends Application {
	Button btn0;
	Button btn1;
	Button btn2;
	Button btn3;
	Button btn4;
	Button btn5;
	Button btn6;
	Button btn7;
	Button btn8;
	Button btn9;
	Button btn_call;
	TextField tf;
	Popup popup;
	Label lbl;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			Parent root = FXMLLoader.load(getClass().getResource("main8.fxml"));
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			btn0 = (Button)scene.lookup("#btn0");
			btn1 = (Button)scene.lookup("#btn1");
			btn2 = (Button)scene.lookup("#btn2");
			btn3 = (Button)scene.lookup("#btn3");
			btn4 = (Button)scene.lookup("#btn4");
			btn5 = (Button)scene.lookup("#btn5");
			btn6 = (Button)scene.lookup("#btn6");
			btn7 = (Button)scene.lookup("#btn7");
			btn8 = (Button)scene.lookup("#btn8");
			btn9 = (Button)scene.lookup("#btn9");
			btn_call = (Button)scene.lookup("#btn_call");
			tf = (TextField)scene.lookup("#tf");
			
			
			btn_call.setOnMouseClicked(new EventHandler<Event>() {
				String result = "";

				@Override
				public void handle(Event event) {
					result = tf.getText();
					popup = new Popup();
					try {
						Parent root_popup = FXMLLoader.load(getClass().getResource("main8_popup.fxml"));
						Scene scene_popup = new Scene(root_popup, 400, 400);
						scene_popup.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
						popup.getContent().add(root_popup);
						lbl = (Label)scene_popup.lookup("#lbl");
						
					} catch (IOException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
					
					popup.show(primaryStage);
					
					System.out.println(btn0.getText());
					lbl.setText(result + "에게 전화를 거는 중입니다.......");
					
				}
			});
			
			btn0.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					tf.setText("" + tf.getText() + btn0.getText());
				}
			});
			btn1.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					tf.setText("" + tf.getText() + btn1.getText());
				}
			});
			btn2.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					tf.setText("" + tf.getText() + btn2.getText());
				}
			});
			btn3.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					tf.setText("" + tf.getText() + btn3.getText());
				}
			});
			btn4.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					tf.setText("" + tf.getText() + btn4.getText());
				}
			});
			btn5.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					tf.setText("" + tf.getText() + btn5.getText());
				}
			});
			btn6.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					tf.setText("" + tf.getText() + btn6.getText());
				}
			});
			btn7.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					tf.setText("" + tf.getText() + btn7.getText());
				}
			});
			btn8.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					tf.setText("" + tf.getText() + btn8.getText());
				}
			});
			btn9.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					tf.setText("" + tf.getText() + btn9.getText());
				}
			});
			
			primaryStage.setScene(scene);
			primaryStage.show();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public static void main(String[] args) {
		launch(args);
	}
	
	
}
