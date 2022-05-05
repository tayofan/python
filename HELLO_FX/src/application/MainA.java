package application;
	
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.Set;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.stage.Stage;


public class MainA extends Application {
	Button btn;
	TextField tf;
	TextArea ta;
	String com;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			Parent root = FXMLLoader.load(getClass().getResource("mainA.fxml"));
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			btn = (Button) scene.lookup("#btn");
			tf = (TextField) scene.lookup("#tf");
			ta = (TextArea) scene.lookup("#ta");
			randomNum();
			btn.setOnMouseClicked(new EventHandler<Event>() {

				@Override
				public void handle(Event event) {
					playGame();
					tf.setText(null);
					
				}
			});
			
			tf.setOnKeyPressed(new EventHandler<KeyEvent>() {

				@Override
				public void handle(KeyEvent event) {
					if(event.getCode() == KeyCode.ENTER) {
						playGame();
						tf.setText(null);
					}
					
				}
			});
			
			primaryStage.setScene(scene);
			primaryStage.show();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	private void playGame() {
		String result_old = ta.getText();
		String result_new = getResult();
//		String my = tf.getText();
//		
//		int s = 0;
//		int b = 0;
//		int o = 3;
//		
//		if(my.charAt(0) == com.charAt(0)) s++;
//		if(my.charAt(0) == com.charAt(1)) b++;
//		if(my.charAt(0) == com.charAt(2)) b++;
//		
//		if(my.charAt(1) == com.charAt(0)) b++;
//		if(my.charAt(1) == com.charAt(1)) s++;
//		if(my.charAt(1) == com.charAt(2)) b++;
//		
//		if(my.charAt(2) == com.charAt(0)) b++;
//		if(my.charAt(2) == com.charAt(1)) b++;
//		if(my.charAt(2) == com.charAt(2)) s++;
//		
//		o -= s + b;
//		result = result_old + my + "-" + s + "S" + b + "B" + o + "O\n";
//		
//		if(s == 3) {
//			win();
//			return;
//		}
		if(result_new == null) {
			win();
			return;
		}

		
		ta.setText(result_old + result_new);
	}
	
	private String getResult() {
		String result;
		String my = tf.getText();
		
		int s = 0;
		int b = 0;
		int o = 3;
		
		if(my.charAt(0) == com.charAt(0)) s++;
		if(my.charAt(0) == com.charAt(1)) b++;
		if(my.charAt(0) == com.charAt(2)) b++;
		
		if(my.charAt(1) == com.charAt(0)) b++;
		if(my.charAt(1) == com.charAt(1)) s++;
		if(my.charAt(1) == com.charAt(2)) b++;
		
		if(my.charAt(2) == com.charAt(0)) b++;
		if(my.charAt(2) == com.charAt(1)) b++;
		if(my.charAt(2) == com.charAt(2)) s++;
		
		
		o -= s + b;
		result = my + "-" + s + "S" + b + "B" + o + "O\n";
		if(s == 3) return null;
		return result;
	}
	
	private void win() {
		String str_tel = tf.getText();
		Alert alert = new Alert(AlertType.INFORMATION);
		alert.setTitle("이겼습니다.");
		alert.setHeaderText(null);
		alert.setContentText(str_tel);

		alert.showAndWait();
	}
	
	private void randomNum() {
		Set<String> set = new HashSet<String>();
		int random;
		String num = "";
		while(true) {
			if(set.size() >= 3) break;
			random = (int)(Math.random() * 10);
			num = "" + random;
			set.add(num);
			
		}
		
		num = "";
		ArrayList<String> list = new ArrayList<String>(set);
		Collections.shuffle(list);
		for(String str : list) {
			num += str;
		}
		com = num;
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
