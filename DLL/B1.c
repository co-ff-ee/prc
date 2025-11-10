#include <jni.h>
#include "B1.h"

JNIEXPORT jint JNICALL Java_B1_add(JNIEnv *env, jobject obj, jint a, jint b) {
    return a + b;
}

JNIEXPORT jint JNICALL Java_B1_sub(JNIEnv *env, jobject obj, jint a, jint b) {
    return a - b;
}

JNIEXPORT jint JNICALL Java_B1_mult(JNIEnv *env, jobject obj, jint a, jint b) {
    return a * b;
}

JNIEXPORT jdouble JNICALL Java_B1_div(JNIEnv *env, jobject obj, jint a, jint b) {
    return (jdouble)a / b;
}

