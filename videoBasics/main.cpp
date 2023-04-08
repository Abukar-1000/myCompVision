#include <iostream>
#include <opencv2/opencv.hpp>

int main(int, char**) {
    std::string basePath = "Computer-Vision-py/DATA/";
    cv::Mat img = cv::imread("Computer-Vision-py/DATA/sudoku.jpg", 0);
    cv::imshow("img", img);
    std::cout << "Hello, world!\n";
}
