#include <iostream>
#include "C:/Users/Abuka/vcpkg/installed/x86-windows/include/opencv2/opencv.hpp"

int main() {
    std::string basePath = "Computer-Vision-py/DATA/";
    cv::Mat img = cv::imread("Computer-Vision-py/DATA/sudoku.jpg", 0);
    cv::imshow("img", img);
    return 0;
}